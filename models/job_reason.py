from odoo import fields, models


class JobReason(models.Model):
    _name = 'job.reason'
    _description = 'AC Service'

    name = fields.Char(string="Name")
    reason_type = fields.Selection([
        ('cancel', 'Cancel'),
        ('rescheduled', 'Rescheduled')], string="Reason Type")
