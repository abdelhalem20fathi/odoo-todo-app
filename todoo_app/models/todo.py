from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To Do Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date')
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='new')
