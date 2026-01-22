from odoo import models, fields, api
from datetime import date, timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: date.today() + timedelta(days=90))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    total_area = fields.Integer(compute='_compute_total_area')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    active = fields.Boolean(default=True)
    state = fields.Selection([
        {'new','New'},
        {'offer_received','Offer received'},
        {'offer_accepted','Offer accepted'},
        {'sold','Sold'},
        {'cancelled','Cancelled'},
    ])
    garden_orientation = fields.Selection([
        {'north','North'},
        {'south','South'},
        {'east','East'},
        {'west','West'},
    ])
    property_type_id = fields.Many2one('estate.property.type')
    buyer_id = fields.Many2one('res.partner' , copy=False)
    seller_id = fields.Many2one('res.users', default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')
    best_price = fields.Float(compute='_compute_best_price')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0) + (record.garden_area or 0)
    
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for prop in self:
            prices = prop.mapped('offer_ids.price')
            prop.best_price = max(prices) if prices else 0