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


# class hardsail(models.Model):
#     _name = 'hardsail.hardsail'
#     _description = 'hardsail.hardsail'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
