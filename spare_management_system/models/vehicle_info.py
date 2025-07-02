from odoo import models, fields


class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _rec_name="name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char("Vehicle Name",requied="true")
    type=fields.Char("Vehicle Type")
    make=fields.Char("Make")
    model_name=fields.Char("Model")
    model_year=fields.Integer("Year")
    order_lines = fields.One2many("vehicle.order.lines", "vehicle", "Order lines")



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

