from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    is_hardware = fields.Boolean(
        string='Hardware Component',
        default=False,
        store=True,
        index=True
    )

    component_type = fields.Selection(
        selection=[
            ('cpu', 'CPU'),
            ('gpu', 'GPU'),
            ('ram', 'RAM'),
            ('storage', 'Storage'),
            ('motherboard', 'Motherboard')
        ],
        string='Component Type',
        store=True,
        index=True
    )