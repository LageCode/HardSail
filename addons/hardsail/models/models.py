# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class ProductCategory(models.Model):
    _inherit = 'product.category'

    attribute_ids = fields.Many2many(
        'product.attribute',
        string='Attributes',
        help="Attributes applicable for products in this category."
    )


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.onchange('categ_id')
    def _onchange_categ_id(self):
        if self.categ_id:
            self.attribute_line_ids = [(5, 0, 0)]  # Clear existing attributes
            self.attribute_line_ids = [
                (0, 0, {'attribute_id': attr.id}) for attr in self.categ_id.attribute_ids
            ]


class ComponentCompatibility(models.Model):
    _name = 'component.compatibility'
    _description = 'Component Compatibility Rules'

    name = fields.Char(string='Rule Name', required=True)
    category_id = fields.Many2one('product.category', string='Component Category', required=True)
    compatible_category_id = fields.Many2one('product.category', string='Compatible With', required=True)
    attribute_id = fields.Many2one('product.attribute', string='Matching Attribute', required=True)


class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    categ_id = fields.Many2one(
        'product.category',
        string='Product Category',
        related='product_id.categ_id',
        store=True,
        readonly=True,
        help="Category of the selected product."
    )

    attribute_value_ids = fields.Many2many(
        'product.template.attribute.value',
        string='Attributes',
        related='product_id.product_template_attribute_value_ids',
        readonly=True
    )


class PCConfiguration(models.Model):
    _name = 'pc.configuration'
    _description = 'PC Configuration'

    name = fields.Char(string='Name')
    bom_id = fields.Many2one('mrp.bom', string='Bill of Materials')
    manufacturing_order_id = fields.Many2one('mrp.production', string='Manufacturing Order')

    @api.constrains('bom_id')
    def _check_bom_compatibility(self):
        self._check_component_compatibility()

    state = fields.Selection([
        ('draft', 'Draft'),
        ('validated', 'Validated'),
        ('manufacturing', 'In Production'),
        ('done', 'Done')
    ], default='draft')
    bom_line_ids = fields.One2many(
        related='bom_id.bom_line_ids',
        string='BOM Lines',
        readonly=True
    )

    total_price = fields.Float(compute='_compute_total_price')

    @api.depends('bom_id.bom_line_ids.product_tmpl_id')
    def _compute_total_price(self):
        for record in self:
            record.total_price = sum(line.product_id.lst_price * line.product_qty 
                                   for line in record.bom_id.bom_line_ids)
                
    def action_validate(self):
        self._check_component_compatibility()
        self.write({'state': 'validated'})

    def action_start_manufacturing(self):
        self.ensure_one()
        if not self.bom_id:
            raise ValidationError("Please select a Bill of Materials first.")
            
        if self.state == 'validated' and not self.manufacturing_order_id:
            mo_vals = {
                'product_id': self.bom_id.product_tmpl_id.product_variant_id.id,
                'bom_id': self.bom_id.id,
                'product_qty': 1.0,
                'product_uom_id': self.bom_id.product_uom_id.id,
            }
            mo = self.env['mrp.production'].create(mo_vals)
            self.write({
                'manufacturing_order_id': mo.id,
                'state': 'manufacturing'
            })
            mo.action_confirm()

    def action_mark_done(self):
        self.ensure_one()
        if self.manufacturing_order_id:
            self.manufacturing_order_id.button_mark_done()
        self.write({'state': 'done'})

    def _check_component_compatibility(self):
        _logger.info('---Checking component compatibility---')
        for config in self:
            if not config.bom_id:
                continue
                
            components = config.bom_id.bom_line_ids.mapped('product_id')
            _logger.info('Components to check: %s', components)
            
            # Initialize dictionaries to track components by socket/DDR
            socket_components = {}
            ddr_components = {}

            # Check each component
            for comp in components:
                # Get socket attribute
                socket_attrs = comp.product_template_attribute_value_ids.filtered(
                    lambda x: x.attribute_id.name.lower() == 'socket'
                )
                if socket_attrs:
                    socket = socket_attrs[0].name
                    if socket not in socket_components:
                        socket_components[socket] = []
                    socket_components[socket].append(comp.name)

                # Get DDR attribute
                ddr_attrs = comp.product_template_attribute_value_ids.filtered(
                    lambda x: x.attribute_id.name.lower() == 'ddr'
                )
                if ddr_attrs:
                    ddr = ddr_attrs[0].name
                    if ddr not in ddr_components:
                        ddr_components[ddr] = []
                    ddr_components[ddr].append(comp.name)

            _logger.info('Socket components: %s', socket_components)
            _logger.info('DDR components: %s', ddr_components)
            
            # Check socket compatibility
            if len(socket_components) > 1:
                error_msg = "Incompatible sockets found:\n"
                for socket, comps in socket_components.items():
                    error_msg += f"- Socket {socket}: {', '.join(comps)}\n"
                raise ValidationError(error_msg)
            
            # Check DDR compatibility
            if len(ddr_components) > 1:
                error_msg = "Incompatible DDR types found:\n"
                for ddr, comps in ddr_components.items():
                    error_msg += f"- DDR {ddr}: {', '.join(comps)}\n"
                raise ValidationError(error_msg)

    @api.model
    def create(self, vals):
        _logger.info('---START Creating new PC Configuration---')
        _logger.info('Incoming vals: %s', vals)  # Log of received data
        vals['name'] = self.env['ir.sequence'].next_by_code('pc.configuration')
        _logger.info('Generated name: %s', vals['name'])
        result = super().create(vals)
        return result
