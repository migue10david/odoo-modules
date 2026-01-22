from odoo import models, fields, api

class BarbershopAppointment(models.Model):
    _name = 'barbershop.appointment'
    _description = 'Cita'

    name = fields.Char(string='Nombre', required=True)
    client_id = fields.Many2one('barbershop.client', string='Cliente', required=True)
    barber_id = fields.Many2one('barbershop.barber', string='Barbero', required=True)
    service_id = fields.Many2one('barbershop.service', string='Servicio', required=True)
    date = fields.Date(string='Fecha', required=True)
    price = fields.Float(string='Precio', required=True, related='service_id.price')