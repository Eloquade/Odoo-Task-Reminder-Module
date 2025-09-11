from odoo import http
from odoo.http import request

class TaskReminderController(http.Controller):

    @http.route('/task_reminder/tasks', type='http', auth='user', website=True)
    def task_page(self):
        # Load your custom model
        tasks = request.env['task.reminder'].sudo().search([])
        return request.render(
            'task_reminder.task_template',   # XML template ID
            {'tasks': tasks}                 # Data passed into QWeb
        )
