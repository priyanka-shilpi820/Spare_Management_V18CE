from odoo import models, fields,api
import logging
_logger = logging.getLogger(__name__)


class Spare(models.Model):
    _inherit = 'product.template'

    brand = fields.Char(string='Brand', required=True)
    part_number = fields.Char(string='CODE',default=lambda self: 'New', readonly=True, copy=False)
    part_name = fields.Char(string='Part Name')
    description = fields.Char(string='Description')
    model_name = fields.Many2one("vehicle.information", "Vehicle")
    unit_of_measure = fields.Integer("UOM")
    cost_price = fields.Integer("Cost Price")
    sale_price = fields.Integer("Sales Price")
    whole_sale_price = fields.Integer("Whole SalePrice")
    image = fields.Binary("Image")
    year = fields.Char(string='Year')

    vehicle_ids = fields.One2many(
        comodel_name="product.vehicle",
        inverse_name="product_id",
        string="Common Products"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            _logger.info("Before seq, vals: %r", vals)
            if vals.get('part_number') == 'New':
                seq = self.env['ir.sequence'].sudo().next_by_code('product.template.part_number')
                _logger.info("Generated seq: %r", seq)
                vals['part_number'] = seq or 'New'
            _logger.info("After seq, vals: %r", vals)
        return super().create(vals_list)


class ProductVehicle(models.Model):
    _name = "product.vehicle"
    product_id = fields.Many2one("product.template", string="Product")
    # makes = fields.Many2one("vehicle.info", string="Make")
    models = fields.Many2one("vehicle.information",string="Model")
    start_year = fields.Integer(string="Start year")
    end_year = fields.Integer(string="End year")