from odoo import models, fields, api
from datetime import datetime, timedelta

class Task(models.Model):
    _name = 'task.reminder'
    _description = 'Task with Reminder'
    
    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Datetime(string='Deadline', required=True)
    is_completed = fields.Boolean(string='Completed', default=False)
    personal_task_id = fields.Many2one('personal.task', string='Related Personal Task')
    
    def check_deadline(self):
        now = fields.Datetime.now()
        soon = now + timedelta(hours=1)
        task = self.search([('deadline', '<=', soon), ('is_completed', '=', False)])
        for task in task:
            _logger = self.env['ir.logging']
            _logger.create({
                'name': 'Task Reminder',
                'type': 'server',
                'dbname': self._cr.dbname,
                'level': 'INFO',
                'message': f"Reminder: Task '{task.name}' is due soon!",
                'path': __name__,
                'line': '0',
                'func': 'check_deadline',
            })