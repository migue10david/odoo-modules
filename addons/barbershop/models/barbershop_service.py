from odoo import models, fields

class BarbershopService(models.Model):
    _name = 'barbershop.service'
    _description = 'Servicio'

    name = fields.Char(string='Nombre', required=True)
    price = fields.Float(string='Precio', required=True)
    duration = fields.Float(string='Duración', required=True, default=0.5)