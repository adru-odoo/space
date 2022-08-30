# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectForm(models.Model):
    _inherit = 'project.project'
    
    mission_id = fields.Many2one(comodel_name='space.mission',
                                string='Related Space Mission',
                                ondelete='set null')
    
    crew_size = fields.Integer(string='Crew Size',
                              related='mission_id.crew_size')
    
    captain_id = fields.Many2one(string='Mission Captain',
                                related='mission_id.captain_id')
    
    crew_ids = fields.Many2many(string='Crew',
                               related='mission_id.crew_ids')