from odoo import models, fields

class VehicleType(models.Model):
    _name = 'vehicle.type'
    _description = 'Vehicle Type'

    name = fields.Char(required=True)


class VehicleMake(models.Model):
    _name = 'vehicle.make'
    _description = 'Vehicle Make'

    name = fields.Char(required=True)

class VehicleModel(models.Model):
    _name = 'vehicle.model'
    _description = 'Vehicle Model'

    name = fields.Char(required=True)
    make_id = fields.Many2one('vehicle.make', string='Make', required=True)
    type_id = fields.Many2one('vehicle.type', string='Type')


class VehicleYear(models.Model):
    _name = 'vehicle.year'
    _description = 'Vehicle Make'

    name = fields.Char(required=True)

