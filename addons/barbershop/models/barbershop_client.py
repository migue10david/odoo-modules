from odoo import models, fields

class BarbershopClient(models.Model):
    _name = 'barbershop.client'
    _description = 'Cliente de Barbería'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Teléfono', required=True)
    appointements_ids = fields.One2many('barbershop.appointment', 'client_id', string='Citas')
    note = fields.Text(string='Notas')
    color = fields.Integer(string='Color', default=0)