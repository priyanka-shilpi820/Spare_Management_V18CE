from odoo import models, fields


class Spare(models.Model):
    _inherit = 'product.template'

    brand = fields.Char(string='Brand', required=True)
    part_number = fields.Char(string='CODE', required=True)
    part_name = fields.Char(string='Part Name')
    description = fields.Char(string='Description')
    model_name = fields.Many2one("vehicle.information", "Vehicle")
    unit_of_measure = fields.Integer("UOM")
    cost_price = fields.Integer("Cost Price")
    sale_price = fields.Integer("Sales Price")
    whole_sale_price = fields.Integer("Whole SalePrice")
    image = fields.Binary("Image")
    year = fields.Char(string='Year')

    vehicle_ids = fields.One2many(
        comodel_name="product.vehicle",
        inverse_name="product_id",
        string="Common Products"
    )

class ProductVehicle(models.Model):
    _name = "product.vehicle"
    product_id = fields.Many2one("product.template", string="Product")
    # makes = fields.Many2one("vehicle.info", string="Make")
    models = fields.Many2one("vehicle.information",string="Model")
    start_year = fields.Integer(string="Start year")
    end_year = fields.Integer(string="End year")