from odoo import models, fields


class Spare(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand', required=True,string='brand')
    # part_number = fields.Char(string='CODE', required=True)
    # part_name = fields.Char(string='Part Name')
    # description = fields.Char(string='Description')
    # model_name = fields.Many2one("vehicle.information", "Vehicle")
    # unit_of_measure = fields.Integer("UOM")
    # cost_price = fields.Integer("Cost Price")
    # sale_price = fields.Float("Sales Price")
    whole_sale_price = fields.Integer(string="Whole Sale Price")
    # image = fields.Binary("Image")
    # year = fields.Char(string='Year')

