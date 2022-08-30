# -*- coding: utf-8 -*-

from odoo import http


class Space(http.Controller):
    @http.route('/space/', auth='public', website=True)
    def index(self, **kw):
        return 'yes'

    @http.route('/space/missions', auth='public', website=True)
    def courses(self, **kw):
        missions = http.request.env['space.mission'].search([])
        return http.request.render('odoo-space.mission_website', {
                'missions': missions
            })
