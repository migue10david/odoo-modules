from odoo import models, fields, api

class ShippingOrderLine(models.Model):
    _name = 'shipping.order.line'
    _description = 'Línea de envío'

    order_id = fields.Many2one(
        'shipping.order',
        string='Orden de envío',
        required=True,
        ondelete='cascade'
    )

    product_id = fields.Many2one(
    'product.product',
    string='Producto',
    ondelete='restrict'
    )

    product_name = fields.Char(
    string='Descripción',
    compute='_compute_product_name',
    store=True
    )

    quantity = fields.Integer(
        string='Cantidad',
        default=1
    )

    weight_lb = fields.Float(
        string='Peso (lb)',
        required=True
    )

    declared_value = fields.Monetary(
        string='Valor declarado',
        currency_field='currency_id'
    )

    currency_id = fields.Many2one(
        related='order_id.currency_id',
        store=True
    )

    @api.depends('product_id')
    def _compute_product_name(self):
        for line in self:
            line.product_name = line.product_id.display_name if line.product_id else False