from odoo import models, fields

class PersonalTask(models.Model):
    _name = 'personal.task'
    _description = 'Personal Task'
    _order = 'priority desc, due_date asc'

    title = fields.Char(string='Task', required=True)
    notes = fields.Text(string='Notes')
    due_date = fields.Date(string='Due Date')
    completed = fields.Boolean(string='Done', default=False)
    completed_date = fields.Datetime(string='Completed On')

    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority', default='medium')

    userid = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    color = fields.Integer(string='Color', default=0)