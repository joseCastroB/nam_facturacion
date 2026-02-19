{
    'name': 'NAM Facturación Personalizada',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Personalización de vistas de facturas de proveedor',
    'depends': ['account', 'analytic'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
}