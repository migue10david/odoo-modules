{
    'name': 'Barbershop',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manage Barbershop',
    'author': 'Miguel David',
    'description': 'Nuevo módulo de ejemplo',
    'license': 'LGPL-3',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/barbershop_client_view.xml',
        'views/barbershop_barber_view.xml',
        'views/barbershop_service.xml',
        'views/barbershop_appointment_view.xml',
        'views/barbershop_menu.xml',
    ]
}