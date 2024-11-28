from odoo import models, fields, api

class Manufacturer(models.Model):
    _name = 'manufacturer'
    _description = 'Manufacturer'
    
    name = fields.Char(string='Name', required=True)

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
        ('storage', 'Storage'),
        ('case', 'Case'),
        ('powersupply', 'PowerSupply')
    ], string='Component Type')

    manufacturer = fields.Many2one('manufacturer', string='Manufacturer')

    def _get_category(self, type_name):
        """Get or create the product category based on type."""
        hardware_category = self.env['product.category'].search([('name', '=', 'Hardware')], limit=1)
        if not hardware_category:
            hardware_category = self.env['product.category'].create({'name': 'Hardware'})
        return self.env['product.category'].search([
            ('name', '=', type_name),
            ('parent_id', '=', hardware_category.id)
        ], limit=1) or self.env['product.category'].create({
            'name': type_name,
            'parent_id': hardware_category.id
        })

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

    @api.model
    def create(self, vals):
        vals['categ_id'] = self._get_category('CPU').id
        return super(CPU, self).create(vals)

    @api.model
    def write(self, vals):
        vals['categ_id'] = self._get_category('CPU').id
        return super(CPU, self).write(vals)

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

    @api.model
    def create(self, vals):
        vals['categ_id'] = self._get_category('GPU').id
        return super(GPU, self).create(vals)

    @api.model
    def write(self, vals):
        vals['categ_id'] = self._get_category('GPU').id
        return super(GPU, self).write(vals)

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

    @api.model
    def create(self, vals):
        vals['categ_id'] = self._get_category('RAM').id
        return super(GPU, self).create(vals)

    @api.model
    def write(self, vals):
        vals['categ_id'] = self._get_category('RAM').id
        return super(GPU, self).write(vals)

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

    @api.model
    def create(self, vals):
        vals['categ_id'] = self._get_category('Motherboard').id
        return super(Motherboard, self).create(vals)

    @api.model
    def write(self, vals):
        vals['categ_id'] = self._get_category('Motherboard').id
        return super(Motherboard, self).write(vals)

class Case(models.Model):
    _inherit = 'product.template'
    
    case_form_factor = fields.Selection([
        ('full_tower', 'Full Tower'),
        ('mid_tower', 'Mid Tower'),
        ('mini_tower', 'Mini Tower')
    ], string='Form Factor')

    case_max_gpu_length = fields.Integer(string='Max GPU Length (mm)')
    case_max_psu_length = fields.Integer(string='Max PSU Length (mm)')
    case_included_fans = fields.Integer(string='Included Fans')
    case_max_fans = fields.Integer(string='Maximum Fan Support')

    @api.model
    def create(self, vals):
        vals['categ_id'] = self._get_category('Case').id
        return super(Case, self).create(vals)

    @api.model
    def write(self, vals):
        vals['categ_id'] = self._get_category('Case').id
        return super(Case, self).write(vals)

class PowerSupply(models.Model):
    _inherit = 'product.template'
    
    psu_wattage = fields.Integer(string='Wattage')
    psu_efficiency = fields.Selection([
        ('80plus', '80 PLUS'),
        ('80plus_bronze', '80 PLUS Bronze'),
        ('80plus_silver', '80 PLUS Silver'),
        ('80plus_gold', '80 PLUS Gold'),
        ('80plus_platinum', '80 PLUS Platinum'),
        ('80plus_titanium', '80 PLUS Titanium')
    ], string='Efficiency Rating')
    psu_modular = fields.Selection([
        ('full', 'Fully Modular'),
        ('semi', 'Semi Modular'),
        ('none', 'Non Modular')
    ], string='Modularity')
    psu_form_factor = fields.Selection([
        ('atx', 'ATX'),
        ('sfx', 'SFX'),
        ('sfx_l', 'SFX-L')
    ], string='Form Factor')

    @api.model
    def create(self, vals):
        vals['categ_id'] = self._get_category('PSU').id
        return super(PowerSupply, self).create(vals)

    @api.model
    def write(self, vals):
        vals['categ_id'] = self._get_category('PSU').id
        return super(PowerSupply, self).write(vals)