# -*- coding: utf-8 -*-
{
    'name': 'Custom Product Management',
    'category': 'employees',
    'author': 'Reliution',
    'version': '15.0.0.2',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base', 'product','base_setup'],
    'data': ['security\ir.model.access.csv',
             'view\general_settings.xml',
             'view\import_process_view.xml',
             'view\part_code.xml',
             'view\product.category.xml',
             'view\product.xml',
             'view\product_specification.xml',
             'view\products.import.history.xml',
             'view\search.term.xml'],
    'auto_install': False,
    'application': True,
    'installable': True,
}

