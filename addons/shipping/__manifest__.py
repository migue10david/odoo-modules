{
    'name': 'Envíos USA a Cuba',
    'version': '1.0',
    'summary': 'Gestión de envíos de paquetes por peso (Libras) desde USA a Cuba',
    'category': 'Inventory/Logistics',
    'author': 'Miguel David',
    'depends': [
        'base',
        'product',
        'account',  # Necesario para generar facturas
        'mail',     # Para el chatter (historial y mensajes)
    ],
    'data': [
        'security/ir.model.access.csv',      # Permisos de acceso
        'data/shipping_order_sequence.xml',         # Para que los pedidos sean ENV-001, ENV-002...
        'views/shipping_partner_view.xml',
        'views/shipping_rate_views.xml',
        'views/shipping_order_views.xml',
        'views/shipping_order_line_views.xml',
        'views/shipping_menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}