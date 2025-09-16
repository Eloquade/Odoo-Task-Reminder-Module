from odoo import models, fields

class Tag(models.Model):
    _name = 'task.tag'
    _description = 'Task Tag'

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color', default=0)