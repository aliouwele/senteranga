# -*- coding: utf-8 -*-
{
    'name': "senteranga",

    'summary': """
    All in one senteranga""",

    'description': """
        All in one senteranga
    """,

    'author': "Aliou Samba Wele",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'purchase', 'purchase_stock', 
        'point_of_sale', 'sh_product_multi_barcode', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/pos_assets_common.xml',
        'data/template_mail.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
