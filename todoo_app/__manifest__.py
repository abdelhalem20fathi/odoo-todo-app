{
    'name': 'To-Do App',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'A simple to-do app',
    'description': 'A simple to-do list app for managing tasks in Odoo.',
    'author': 'Abdelhalem Fathi',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_view.xml',
    ],
    'installable': True,
    'application': True,
}
