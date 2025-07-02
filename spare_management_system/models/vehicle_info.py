from odoo import models, fields


class Vehicle(models.Model):
    _name = 'vehicle.info'
    _description = 'Vehicle Information'
    _rec_name='model_name'

    model_name = fields.Char(string='Model', required=True)
    manufacturer_id = fields.Many2one('vehicle.manufacturer', string='Manufacturer', required=True)
    year = fields.Char(string='Year')
    engine_variant = fields.Char(string='Engine / Variant')
    product_ids = fields.One2many(
        'product.template',
        'vehicle_model_id',
        string='Products'
    )

    def action_add_existing_products(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Add Existing Products',
            'res_model': 'add.products.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_vehicle_id': self.id,
            }
        }