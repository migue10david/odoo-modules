from odoo import models, fields

class BarbershopAccessory(models.Model):
    _name = 'barbershop.accessory'
    _description = 'Accesorio'

    name = fields.Char(string='Nombre', required=True)
    is_active = fields.Boolean(string='Activo', default=True)
    barber_id = fields.Many2one('barbershop.barber', string='Barbero', required=True)