# -*- coding: utf-8 -*-

{
    'name': 'Odoo Space',
    
    'summary': "App to plan Odoo's first moon landing",
    
    'description': "goin to space",
    
    'author': 'wadam',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Spaceflight',
    
    'version': '0.1',
    
    'depends': ['project', 'website'],
    
    'license': 'OPL-1',
    
    'data': [
        'security/space_security.xml',
        'security/ir.model.access.csv',
        'views/space_menuitems.xml',
        "views/spaceship_views.xml",
        "views/mission_views.xml",
        "views/project_views_inherit.xml",
        "views/space_web_templates.xml",
        "report/spaceship_report_templates.xml"
    ],
    
    'demo': ['demo/space_demo.xml']
}
