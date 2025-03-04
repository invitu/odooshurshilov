# -*- coding: utf-8 -*-
# Copyright (C) 2021 Artem Shurshilov <shurshilov.a@yandex.ru>
{
    'name': "Login in Odoo from URL (by link)",

    'summary': """
        Login in Odoo from URL or link for example if we want open contacts:
        https://eurodoo.com/login_employee?login=demo1&amp;password=demo1&amp;action=contacts.action_contacts""",

    'author': "EURO ODOO, EURO ODOO, Shurshilov Artem",
    'website': "https://eurodoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '14.0.0.0',
    "license": "LGPL-3",
    'images': [
        'static/description/example.gif'
    ],

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'installable': True,

}
