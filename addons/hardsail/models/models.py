# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ComponentTemplate(models.Model):
    _name = 'component.template'
    _description = 'Component Template'

    name = fields.Char(string='Component Name', required=True)
    property_ids = fields.Many2many('component.property', string='Properties')


class ComponentProperty(models.Model):
    _name = 'component.property'
    _description = 'Component Property'

    name = fields.Char(string='Property Name', required=True)
    type = fields.Selection([
        ('string', 'String'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
        ('selection', 'Selection')
    ], string='Property Type', required=True)
    option_ids = fields.One2many('component.property.option', 'property_id', string='Options')

    @api.constrains('type', 'option_ids')
    def _check_options_for_selection(self):
        for record in self:
            if record.type != 'selection' and record.option_ids:
                raise ValidationError("Options can only be added to properties of type 'Selection'")

    @api.onchange('type')
    def _onchange_type(self):
        """
        Resets the option_ids field when the property type is changed in the view.
        """
        if self.type != 'selection':
            self.option_ids = [(5, 0, 0)]  # Clears existing options

    @api.onchange('option_ids')
    def _onchange_options(self):
        if self.type != 'selection' and self.option_ids:
            self.type = 'selection'
            return {
                'warning': {
                    'title': 'Forced type to Selection',
                    'message': 'Options can only be added to properties of type Selection'
                }
            }


class ComponentPropertyOption(models.Model):
    _name = 'component.property.option'
    _description = 'Component Property Option'

    name = fields.Char(string='Option Name', required=True)
    property_id = fields.Many2one('component.property', string='Property')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_hardware = fields.Boolean(string='Is a hardware component', default=False)
    component_id = fields.Many2one('component.template', string='Component Template')
    property_ids = fields.Many2many(related='component_id.property_ids', string='Properties', readonly=True)
    property_value_ids = fields.One2many('product.property.value', 'product_tmpl_id', string='Property Values')
    
    def _sync_property_values(self):
        """Sync property values with component template"""
        self.ensure_one()
        existing_props = {pv.property_id.id: pv for pv in self.property_value_ids}
        
        values = []
        if self.component_id:
            for prop in self.component_id.property_ids:
                if prop.id not in existing_props:
                    values.append((0, 0, {
                        'property_id': prop.id,
                    }))
            
            # Remove properties that don't exist in new component
            for prop_id in existing_props:
                if prop_id not in self.component_id.property_ids.ids:
                    values.append((2, existing_props[prop_id].id, 0))
                    
        if not self.component_id:
            values = [(5, 0, 0)]  # Clear all if no component
            
        if values:
            self.property_value_ids = values

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records:
            if record.is_hardware and record.component_id:
                record._sync_property_values()
        return records

    def write(self, vals):
        res = super().write(vals)
        if 'component_id' in vals:
            for record in self:
                if record.is_hardware:
                    record._sync_property_values()
        return res

    @api.onchange('component_id')
    def _onchange_component_id(self):
        if self.is_hardware:
            self._sync_property_values()


class ProductPropertyValue(models.Model):
    _name = 'product.property.value'
    _description = 'Product Property Value'

    product_tmpl_id = fields.Many2one('product.template', string='Product Template', required=True, ondelete='cascade')
    property_id = fields.Many2one('component.property', string='Property', required=True)
    
    string_value = fields.Char(string='String Value')
    integer_value = fields.Integer(string='Integer Value')
    float_value = fields.Float(string='Float Value')
    boolean_value = fields.Boolean(string='Boolean Value')
    selection_value = fields.Many2one('component.property.option', string='Selection Value')

    @api.onchange('property_id')
    def _onchange_property_id(self):
        # Clear all values when property changes
        self.string_value = False
        self.integer_value = False
        self.float_value = False
        self.boolean_value = False
        self.selection_value = False