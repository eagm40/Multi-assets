# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Multiple Assets Management',
    'depends': ['account_accountant'],
    'sumary': """Let us insert n asset y one invoice""",
    'description': """
Multiple Assets management
=================
Manage multiple assets owned by a company or a person in one invoice.
If you buy n items, you have n assets.
Takes other cost and apply them to the total invoice amount.

    """,
    'author': 'Erick Guerrero',
    'website': 'https://www.meca.com.gt',
    'category': 'Accounting',
    'version': '1.0',
    'sequence': 33,
    'application': True,
#    'demo': [
#        'data/account_asset_demo.yml',
#    ],
    'data': [
        'views/asset_category_multi.xml',
    ],
#    'qweb': [
#        "static/src/xml/account_asset_template.xml",
#    ],
}
