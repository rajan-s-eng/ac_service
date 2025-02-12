from odoo import models, fields, api, _

class AssetService(models.Model):
    _name = 'asset.service'
    _description = 'AC Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='ref', readonly=True, index='trigram', default=lambda self: _('New'))
    company_ref_no = fields.Char(string="Company Refrence No")

    partner_id = fields.Many2one('res.partner', required=True, tracking=True)
    asset_id = fields.Many2one('partner.asset', tracking=True)
    brand_id = fields.Many2one(related="asset_id.brand_id" , store=True)
    model_no = fields.Char(related="asset_id.model_no", store=True)
    warranty_start = fields.Date(related="asset_id.warranty_start", tracking=True)
    warranty_end = fields.Date(related="asset_id.warranty_end", tracking=True)
    schedule_date = fields.Datetime(string="Schedule")
    completion_date = fields.Date(string="Completion Date", tracking=True)
    p_o = fields.Char(string="Po No")
    s_o = fields.Char(string="So No")
    user_id = fields.Many2one('res.users' , string="Technician", tracking=True)
    priority = fields.Char(string="Priority")
    duration = fields.Char(string="Duration")
    cancel_reason_id = fields.Many2one('job.reason',string="Reason")
    cancel_reason = fields.Text(string="Cancel Reason")
    reschedule_reason_id = fields.Many2one('job.reason' ,string="Reschedule Reason")
    reschedule_reason = fields.Text(string="Reason")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('pending_due_to_spare_parts', 'Pending due to Spare Parts'),
        ('rescheduled', 'Rescheduled'),
        ('no_answer', 'No Answer'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ], default='draft', readonly=True, string="Status")

    @api.model_create_multi
    def create(self, vals_list):
        print("\n\n\n")
        print("Create method is called")
        print("Before vals list are : ", vals_list)
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('asset.service') or _("New")
        print("After Vals list are : ", vals_list)
        print("\n\n\n")
        return super().create(vals_list)

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_in_progress(self):
        self.write({'state': 'in_progress'})

    def action_pending_parts(self):
        self.write({'state': 'pending_due_to_spare_parts'})

    def action_completed(self):
        self.write({'state': 'completed'})

    def action_rescheduled(self):
        # self.write({'state': 'rescheduled'})
        ctx = self.env.context.copy()
        action = self.env["ir.actions.act_window"]._for_xml_id("job_service.action_wizard_job_reason")
        ctx.update({
            'default_job_id': self.id,
            'default_reason_type': 'rescheduled'
        })
        action['context'] = ctx
        return action

    def action_no_answer(self):
        self.write({'state': 'no_answer'})

    def action_cancel(self):
        self.ensure_one()
        ctx = self.env.context.copy()
        action = self.env["ir.actions.act_window"]._for_xml_id("job_service.action_wizard_job_reason")
        ctx.update({
            'default_job_id': self.id,
            'default_reason_type': 'cancel'
        })
        action['context'] = ctx
        return action