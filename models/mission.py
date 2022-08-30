# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mission(models.Model):
    _name = 'space.mission'
    _description = 'Mission Information'
    
    name = fields.Char(string='Mission Name', required=True)
    description = fields.Text(string='Description')
    
    vehicle = fields.Many2one(comodel_name='space.spaceship',
                             string='Spaceship',
                             ondelete='set null')
    
    captain_id = fields.Many2one(comodel_name='res.partner', 
                                 string='Captain')
    
    crew_ids = fields.Many2many(comodel_name='res.partner',
                                string='Crew')
    
    launch_date = fields.Datetime(string='Launch Date')
    return_date = fields.Datetime(string='Return Date')
    
    fuel_needed = fields.Float(string='Amount of fuel needed')
    
    distance = fields.Float(string='Distance to Travel')
    
    crew_size = fields.Integer(compute='_compute_crewsize')
    
    @api.depends("crew_ids", "captain_id")
    def _compute_crewsize(self):
        for record in self:
            record.crew_size = len(record.crew_ids) + 1 if record.captain_id else 0
