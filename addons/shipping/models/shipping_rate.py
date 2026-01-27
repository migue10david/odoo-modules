from odoo import models, fields, api

class ShippingRate(models.Model):
    _name = 'shipping.rate'
    _description = 'Tarifas de envío'

    name = fields.Char(required=True)

    transport_type = fields.Selection([
        ('air', 'Aéreo'),
        ('sea', 'Marítimo'),
    ], required=True)

    min_weight_lb = fields.Float(string='Peso mínimo (lb)', default=0)
    max_weight_lb = fields.Float(string='Peso máximo (lb)')

    price_per_lb = fields.Monetary(required=True)
    minimum_price = fields.Monetary(string='Precio mínimo')

    currency_id = fields.Many2one('res.currency', required=True)
    active = fields.Boolean(default=True)