{
    'name': 'Spare Part management',
    "author": "sidmec solutions",
    "license": "LGPL-3",
    'version': '18.0.1.0',
    'summary': 'Manage spare parts and their vehicle compatibility',
    'depends': ['product','sale_management','purchase','stock','sale',],
    'data': [
        'security/ir.model.access.csv',
        'views/product_variants.xml',
        'views/vehicle_view.xml',
        "views/spare_part.xml",
        'views/vehicle_model_view.xml',
        "security/security.xml",
        "views/menu.xml"
    ],
    'installable': True,
    'application': True,
}
