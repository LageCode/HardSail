from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

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
        ('motherboard', 'Motherboard'),
        ('storage', 'Storage')
    ], string='Component Type')

    manufacturer = fields.Selection([
        ('intel', 'Intel'),
        ('amd', 'AMD'),
        ('nvidia', 'NVIDIA'),
        ('msi', 'MSI'),
        ('asus', 'ASUS'),
        ('gigabyte', 'Gigabyte'),
        ('asrock', 'ASRock'),
        ('corsair', 'Corsair'),
        ('kingston', 'Kingston'),
        ('samsung', 'Samsung'),
        ('other', 'Other')
    ], string='Manufacturer')

class CPU(models.Model):
    _inherit = 'product.template'
    
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

class GPU(models.Model):
    _inherit = 'product.template'
    
    gpu_memory = fields.Integer(string='Memory (GB)')
    gpu_type = fields.Selection([
        ('gddr6x', 'GDDR6X'),
        ('gddr6', 'GDDR6'),
        ('gddr5', 'GDDR5')
    ], string='Memory Type')
    gpu_bus = fields.Selection([
        ('pcie4', 'PCIe 4.0'),
        ('pcie3', 'PCIe 3.0')
    ], string='Bus Interface')
    gpu_tdp = fields.Integer(string='TDP (W)')

class RAM(models.Model):
    _inherit = 'product.template'
    
    ram_capacity = fields.Integer(string='Capacity (GB)')
    ram_type = fields.Selection([
        ('ddr5', 'DDR5'),
        ('ddr4', 'DDR4'),
        ('ddr3', 'DDR3')
    ], string='Type')
    ram_speed = fields.Integer(string='Speed (MHz)')
    ram_latency = fields.Char(string='Latency')

class Motherboard(models.Model):
    _inherit = 'product.template'
    
    mb_socket = fields.Selection([
        ('am4', 'AM4'),
        ('am5', 'AM5'),
        ('lga1700', 'LGA 1700'),
        ('lga1200', 'LGA 1200')
    ], string='CPU Socket')
    mb_chipset = fields.Char(string='Chipset')
    mb_form_factor = fields.Selection([
        ('atx', 'ATX'),
        ('matx', 'Micro-ATX'),
        ('itx', 'Mini-ITX')
    ], string='Form Factor')
    mb_ram_slots = fields.Integer(string='RAM Slots')
    mb_ram_type = fields.Selection([
        ('ddr5', 'DDR5'),
        ('ddr4', 'DDR4'),
        ('ddr3', 'DDR3')
    ], string='RAM Type')