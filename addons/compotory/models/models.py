from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Basic hardware fields
    is_hardware = fields.Boolean(
        string='Hardware Component',
        default=False,
        store=True,
        index=True
    )

    component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('motherboard', 'Motherboard')
    ], string='Component Type')

    # CPU Fields
    cpu_brand = fields.Selection([
        ('intel', 'Intel'),
        ('amd', 'AMD')
    ], string='Brand')
    
    cpu_series = fields.Selection([
        ('ryzen3', 'Ryzen 3'),
        ('ryzen5', 'Ryzen 5'),
        ('ryzen7', 'Ryzen 7'),
        ('ryzen9', 'Ryzen 9'),
        ('i3', 'Core i3'),
        ('i5', 'Core i5'),
        ('i7', 'Core i7'),
        ('i9', 'Core i9')
    ], string='Series')
    
    cpu_socket = fields.Selection([
        ('am4', 'AM4'),
        ('am5', 'AM5'),
        ('lga1700', 'LGA 1700'),
        ('lga1200', 'LGA 1200')
    ], string='Socket')
    
    cpu_cores = fields.Integer(string='Number of Cores')
    cpu_threads = fields.Integer(string='Number of Threads')
    cpu_base_clock = fields.Float(string='Base Clock (GHz)')
    cpu_boost_clock = fields.Float(string='Boost Clock (GHz)')
    cpu_cache = fields.Float(string='Cache (MB)')
    cpu_tdp = fields.Integer(string='TDP (W)')
    cpu_integrated_graphics = fields.Boolean(string='Integrated Graphics', default=False)