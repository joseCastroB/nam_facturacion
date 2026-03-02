{
    'name': 'NAM Facturación Personalizada',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Personalización de vistas de facturas de proveedor',
    'depends': ['base','account', 'purchase', 'analytic'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'views/account_analytic_line_views.xml',
    ],
    'installable': True,
    'application': False,
}