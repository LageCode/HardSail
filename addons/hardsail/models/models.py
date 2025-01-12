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
        self.write({'state': 'validated'})

    def action_start_manufacturing(self):
        self.write({'state': 'manufacturing'})

    def action_mark_done(self):
        self.write({'state': 'done'})

    @api.model
    def create(self, vals):
        _logger.info('---START Creating new PC Configuration---')
        _logger.info('Incoming vals: %s', vals)  # Log of received data
        vals['name'] = self.env['ir.sequence'].next_by_code('pc.configuration')
        _logger.info('Generated name: %s', vals['name'])
        result = super().create(vals)
        return result
