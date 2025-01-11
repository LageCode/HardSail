# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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