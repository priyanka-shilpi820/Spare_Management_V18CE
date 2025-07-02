from odoo import models, fields, api

class AddExistingProductsWizard(models.TransientModel):
    _name = 'add.products.wizard'
    _description = 'Add Existing Products to Vehicle'

    vehicle_id = fields.Many2one('vehicle.info', string="Vehicle", required=True)
    product_ids = fields.Many2many('product.template', string="Products")

    def action_add_products(self):
        for product in self.product_ids:
            product.vehicle_model_id = self.vehicle_id.id
        return {'type': 'ir.actions.act_window_close'}