from odoo import models, fields, api, _
from odoo.exceptions import UserError

class WizardJobReason(models.TransientModel):
    _name = 'wizard.job.reason'
    _description = 'Ac service'

    job_id = fields.Many2one("asset.service", string="Job Order")
    reason_id = fields.Many2one('job.reason', string="Reason Type", required=True)
    reason_type = fields.Selection([
        ('cancel', 'Cancel'),
        ('rescheduled', 'Rescheduled')], string="Reason Type")

    reason = fields.Text(string="Reason")

    def action_update_job(self):
        if self.reason_type == 'cancel':
            self.job_id.write({
                'state': 'cancelled',
                'cancel_reason_id': self.reason_id,
                'cancel_reason': self.reason,
            })
        elif self.reason_type == 'rescheduled':
            self.job_id.write({
                'state': 'rescheduled',
                'reschedule_reason_id': self.reason_id,
                'reschedule_reason': self.reason,
            })
