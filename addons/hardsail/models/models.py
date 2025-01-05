# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_hardware = fields.Boolean(string='Is a hardware component', default=False)

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

