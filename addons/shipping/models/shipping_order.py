from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ShippingOrder(models.Model):
    _name = 'shipping.order'
    _description = 'Pedido de envío'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
    string='Referencia',
    required=True,
    readonly=True,
    copy=False,
    default='Nuevo'
    )


    sender_id = fields.Many2one(
        'res.partner',
        string='Cliente remitente',
        required=True,
        domain=[('is_cuban_receiver', '=', False)]
    )

    receiver_id = fields.Many2one(
        'res.partner',
        string='Receptor en Cuba',
        required=True,
        domain=[('is_cuban_receiver', '=', True)]
    )

    transport_type = fields.Selection([
        ('air', 'Aéreo'),
        ('sea', 'Marítimo'),
    ], string='Tipo de transporte', required=True, related='rate_id.transport_type')

    rate_id = fields.Many2one(
        'shipping.rate',
        string='Tarifa aplicada',
        required=True
    )

    currency_id = fields.Many2one(
        related='rate_id.currency_id',
        store=True
    )

    line_ids = fields.One2many(
        'shipping.order.line',
        'order_id',
        string='Productos enviados'
    )

    total_weight_lb = fields.Float(
        string='Peso total (lb)',
        compute='_compute_totals',
        store=True
    )

    total_products_value = fields.Monetary(
        string='Precio de los productos',
        compute='_compute_totals',
        store=True,
        currency_field='currency_id'
    )

    total_amount = fields.Monetary(
        string='Total a pagar',
        compute='_compute_totals',
        store=True,
        currency_field='currency_id'
    )

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('in_transit', 'En tránsito'),
        ('delivered', 'Entregado'),
        ('cancelled', 'Cancelado'),
    ], default='draft', tracking=True)

    @api.depends('line_ids.weight_lb', 'rate_id.price_per_lb', 'line_ids.declared_value')
    def _compute_totals(self):
        for order in self:
            total_weight = sum(order.line_ids.mapped('weight_lb'))
            total_price = sum(order.line_ids.mapped('declared_value'))
            order.total_products_value = total_price
            order.total_weight_lb = total_weight
            order.total_amount = total_weight * order.rate_id.price_per_lb + total_price
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = (
                self.env['ir.sequence'].next_by_code('shipping.order')
                or 'OEUC-ERROR'
        )
        return super().create(vals)



    def action_draft(self):
        for order in self:
            order.state = 'draft'

    def action_confirm(self):
        for order in self:
            if not order.line_ids:
                raise ValidationError('Debe agregar al menos un producto.')
            order.state = 'confirmed'

    def action_in_transit(self):
        for order in self:
            order.state = 'in_transit'

    def action_delivered(self):
        for order in self:
            order.state = 'delivered'

    def action_cancel(self):
        for order in self:
            order.state = 'cancelled'