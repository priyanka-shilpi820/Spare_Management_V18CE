from odoo import models, fields


class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _rec_name="name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char("Vehicle Name",requied=True)
    type=fields.Many2one("vehicle.type","Vehicle Type",required=True)
    make=fields.Many2one("vehicle.make","Make",required=True)
    model_name=fields.Many2one("vehicle.model","Model",required=True)
    model_year=fields.Many2one("vehicle.year","Year",required=True)
    order_lines = fields.One2many("vehicle.order.lines", "vehicle", "Order lines")
    product_id=fields.Many2one('product.product',string='product')



class VehicleorderLines(models.Model):
    _name="vehicle.order.lines"


    product_id=fields.Many2one("product.product","product Name")
    quantity=fields.Integer("qty")
    unit_price=fields.Float("Unitprice")
    vehicle=fields.Many2one("vehicle.information","Vehicle")
    total = fields.Integer("subtotal",compute="compute_sub_total")

    def compute_sub_total(self):
        for rec in self:
            rec.total=rec.quantity * rec.unit_price

