from odoo import models, fields

class TaskOffer(models.Model):
    _name = 'task.offer'
    _description = 'Task Offer'

    task_id = fields.Many2one('task.reminder', string='Task', required=True)
    offer_details = fields.Text(string='Offer Details')
    offered_by = fields.Many2one('res.users', string='Offered By', default=lambda self: self.env.user)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ], string='Status', default='pending')