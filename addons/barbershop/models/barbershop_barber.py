from odoo import models, fields

class BarbershopBarber(models.Model):
    _name = 'barbershop.barber'
    _description = 'Barbero'

    name = fields.Char(string='Nombre', required=True)
    is_active = fields.Boolean(string='Activo', default=True)
    phone = fields.Char(string='Teléfono')
    appointements_ids = fields.One2many('barbershop.appointment', 'barber_id', string='Citas')