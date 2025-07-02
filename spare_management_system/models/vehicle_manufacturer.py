from odoo import models, fields

class VehicleManufacturer(models.Model):
    _name = 'vehicle.manufacturer'
    _description = 'Vehicle Manufacturer'

    name = fields.Char(string='Name', required=True)
    country = fields.Char(string='Country')
    website = fields.Char(string='Website')