from odoo import models, fields

class VehicleManufacturer(models.Model):
    _inherit = 'product.product'

    common_products=fields.Boolean("Common products")

    models = fields.Many2one("vehicle.information", string="Model")
    start_year = fields.Integer(string="Start year")
    end_year = fields.Integer(string="End year")

