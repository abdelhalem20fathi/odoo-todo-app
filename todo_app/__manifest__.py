{
    'name': "TO-DO App New",
    'version': '17.0.0.1.0',
    'depends': ['base','mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
        'reports/todo_task_report.xml',
   ],
    'author': 'Abdelhalem Fathi',
    'installable': True,
    'application': True,
}
