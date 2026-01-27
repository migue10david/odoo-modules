from odoo import models, fields, api

class ShippingPartner(models.Model):
    _inherit = 'res.partner'

    is_cuban_receiver = fields.Boolean(string='Es receptor en Cuba', default=False)
    cuban_ci = fields.Char(string='CI en Cuba', size=11)
    province_cuba = fields.Selection([
        ('Pinar del Río', 'Pinar del Río'),
        ('Artemisa', 'Artemisa'),
        ('La Habana', 'La Habana'),
        ('Mayabeque', 'Mayabeque'),
        ('Matanzas', 'Matanzas'),
        ('Cienfuegos', 'Cienfuegos'),
        ('Villa Clara', 'Villa Clara'),
        ('Sancti Spíritus', 'Sancti Spíritus'),
        ('Ciego de Ávila', 'Ciego de Ávila'),
        ('Camagüey', 'Camagüey'),
        ('Las Tunas', 'Las Tunas'),
        ('Holguín', 'Holguín'),
        ('Granma', 'Granma'),
        ('Santiago de Cuba', 'Santiago de Cuba'),
        ('Guantánamo', 'Guantánamo'),
        ('Isla de la Juventud', 'Isla de la Juventud'),
    ], string='Provincia en Cuba')
    municipality_cuba = fields.Char(string='Municipio en Cuba')

    @api.constrains('is_cuban_receiver', 'cuban_ci', 'province_cuba', 'municipality_cuba')
    def _check_cuban_fields(self):
        for partner in self:
            if partner.is_cuban_receiver:
                if not partner.cuban_ci:
                    raise models.ValidationError('El CI es obligatorio cuando es receptor en Cuba')
                if not partner.province_cuba:
                    raise models.ValidationError('La provincia es obligatoria cuando es receptor en Cuba')
                if not partner.municipality_cuba:
                    raise models.ValidationError('El municipio es obligatorio cuando es receptor en Cuba')
    
    @api.constrains('cuban_ci')
    def _check_cuban_ci_format(self):
        for partner in self:
            if partner.cuban_ci and (not partner.cuban_ci.isdigit() or len(partner.cuban_ci) != 11):
                raise models.ValidationError('La CI cubana debe tener 11 dígitos numéricos')