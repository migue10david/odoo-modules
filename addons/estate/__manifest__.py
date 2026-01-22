{
    'name': 'Real Estate',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Real Estate',
    'author': 'Miguel David',
    'description': 'Nuevo módulo de ejemplo',
    'license': 'LGPL-3',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_menu.xml',
    ]
}