from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    vehicle_model_id = fields.Many2one('vehicle.info', string='Vehicle Model')