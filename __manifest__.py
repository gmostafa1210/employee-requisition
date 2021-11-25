{
    'name': 'Employee Requisition',
    'version': '1.0',
    'sequence': 1,
    'summary': 'Employee Requisition Summary',
    'description': 'Employee Requisition Description.',
    'depends': ['base', 'hr', 'purchase', 'mail'],
    'data': [
        'security/requisition_security.xml',
        'security/ir.model.access.csv',

        'views/requisition_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
