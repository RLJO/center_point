# -*- coding: utf-8 -*-
{
    'name': "Bank & Cash statement Report",

    'summary': """New statement template report for center point company""",

    'description': """New statement template report for center point company""",

    'author': "Ragaa Maher",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/payment_sq_code.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode

}
