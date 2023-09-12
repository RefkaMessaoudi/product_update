# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Product Update',
    'version': '1.0.0',
    'category': 'Products',
    'description': """Product Update""",
    'depends': ['stock'],
    'data': [
             'security/ir.model.access.csv',
             'views/product_update_views.xml',
             'views/menu_views.xml',

             ],
    'images': [
               ],
    'demo': [],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}

