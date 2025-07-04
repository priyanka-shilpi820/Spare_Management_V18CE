from odoo import models, fields,api


class VehicleInformation(models.Model):
    _name = 'vehicle.information'
    _rec_name="name"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char("Vehicle Name",requied=True)
    type=fields.Many2one("vehicle.type","Vehicle Type",requied=True)
    make=fields.Many2one("vehicle.make","Make",requied=True)
    model_name=fields.Many2one("vehicle.model","Model",requied=True)
    model_year=fields.Many2one("vehicle.year", "Year", required=True)
    model_start_year=fields.Char("Start year")
    model_end_year=fields.Char("End year")
    engine_type=fields.Char("Engine/Variant")
    product_id = fields.Many2one('product.product', string='product')
    order_lines = fields.One2many("vehicle.order.lines", "vehicle", "Order lines")


    @api.onchange('model_name')
    def _onchange_model_name(self):
        if self.model_name:
            self.make = self.model_name.make_id
            self.type = self.model_name.type_id






class VehicleorderLines(models.Model):
    _name="vehicle.order.lines"


    product_id=fields.Many2one("product.product","product Name",domain=[('','','')])
    quantity=fields.Integer("qty")
    unit_price=fields.Float("Unitprice")
    vehicle=fields.Many2one("vehicle.information","Vehicle")
    total = fields.Integer("subtotal",compute="compute_sub_total")

    def compute_sub_total(self):
        for rec in self:
            rec.total=rec.quantity * rec.unit_price

