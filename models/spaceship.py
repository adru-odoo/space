# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from pdb import set_trace as bp

class Spaceship(models.Model):

    _name = 'space.spaceship'
    _description = 'Spaceship Information'

    name = fields.Char(string='Spaceship Name', required=True)
    description = fields.Text(string='Description')

    passengers = fields.Integer(string="Passenger Count")

    length = fields.Integer(string="Length", required=True)
    width = fields.Integer(string="Width", required=True)

    active = fields.Boolean(string='Active', default=True)
    
    mission_ids = fields.One2many(comodel_name='space.mission',
                                 inverse_name='vehicle',
                                 string='Mission List')
    
    @api.constrains('width')
    def _check_width_contraint(self):
        for record in self:
            bp()
            if record.width > record.length:
                raise UserError("Spaceship width cannot be greater than length")
                
