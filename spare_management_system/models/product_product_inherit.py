from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'

    compatible_vehicle_ids = fields.Many2many(
        'vehicle.information',
        'product_vehicle_info_rel',
        'product_id', 'vehicle_id',
        string='Compatible Vehicles'
    )
