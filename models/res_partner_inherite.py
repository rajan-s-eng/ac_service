from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Partner(models.Model):
    _inherit = 'res.partner'

    partner_asset_ids = fields.One2many("partner.asset", "partner_id", string="Products")
    product_count = fields.Integer("Product Count", compute="_compute_product_count")

    @api.depends('partner_asset_ids')
    def _compute_product_count(self):
        for partner in self:
            partner.product_count = len(partner.partner_asset_ids)

    def action_partner_assets(self):
        self.ensure_one()
        ctx = self.env.context.copy()
        action = self.env["ir.actions.act_window"]._for_xml_id("job_service.action_partner_asset")
        action['domain'] = [('partner_id', '=', self.id)]
        ctx.update({'default_partner_id': self.id})
        action['context'] = ctx
        return action
