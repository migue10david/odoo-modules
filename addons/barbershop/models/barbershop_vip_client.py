from odoo import models, fields, api

class BarbershopVipClient(models.Model):
    _inherit = 'res.partner'

    is_vip = fields.Boolean(string='VIP' , default=False)
    membership_level = fields.Selection([
        ('gold', 'Gold'),
        ('platinum', 'Platinum'),
        ('diamond', 'Diamond')
    ])
    points = fields.Integer(string='Puntos')
    discount_percentage = fields.Integer(string='Descuento (%)', compute="_compute_discount")

    @api.depends('membership_level')
    def _compute_discount(self):
        for client in self:
            if client.membership_level == 'gold':
                client.discount_percentage = 5
            elif client.membership_level == 'platinum':
                client.discount_percentage = 10
            elif client.membership_level == 'diamond':
                client.discount_percentage = 15
            else:
                client.discount_percentage = 0