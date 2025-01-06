# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ComponentTemplate(models.Model):
    _name = 'component.template'
    _description = 'Component Template'

    name = fields.Char(string='Component Name', required=True)
    property_ids = fields.Many2many('component.property', 'component_template_property_rel', 'component_id', 'property_id', string='Properties')


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
    component_ids = fields.Many2many('component.template', 'component_template_property_rel', 'property_id', 'component_id', string='Component')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_hardware = fields.Boolean(string='Is a hardware component', default=False)
    component_id = fields.Many2one('component.template', string='Component Template')


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

