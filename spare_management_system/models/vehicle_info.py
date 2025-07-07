from odoo import models, fields,api


class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _rec_name="name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char("Vehicle Name",requied="True")
    type=fields.Many2one("vehicle.type","Vehicle Type")
    make=fields.Many2one("vehicle.make","Make")
    model_name=fields.Many2one("vehicle.model","Model")
    model_start_year=fields.Char("Start year")
    model_end_year=fields.Char("End year")
    engine_type=fields.Char("Engine/Variant")
    order_lines = fields.One2many("vehicle.order.lines", "vehicle", "Order lines")


    @api.onchange('model_name')
    def _onchange_model_name(self):
        if self.model_name:
            self.make = self.model_name.make_id
            self.type = self.model_name.type_id






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

