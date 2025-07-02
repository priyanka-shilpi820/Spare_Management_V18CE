{
    'name': 'Spare Part management',
    "author": "sidmec solutions",
    "license": "LGPL-3",
    'version': '18.0.1.0',
    'summary': 'Manage spare parts and their vehicle compatibility',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/vehicle_manufacturer_view.xml',
        'views/vehicle_view.xml',
        'wizard/add_excisting_products_wizard.xml',
        "views/spare_part.xml",
        "views/menu.xml"
    ],
    'installable': True,
    'application': True,
}
