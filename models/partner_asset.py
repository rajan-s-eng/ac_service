from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PartnerAsset(models.Model):
    _name = 'partner.asset'
    _description = 'AC Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Product", required=True, tracking=True)
    indoor_model_sr = fields.Char(string="Indoor Model Sr", tracking=True)
    outdoor_model_sr = fields.Char(string="Outdoor Model Sr", tracking=True)
    purchase_date = fields.Date(string="Purchase Date", tracking=True)
    brand_id = fields.Many2one('asset.brand', string="Brand", required=True)
    invoice_ref = fields.Char(string="Invoice Reference", tracking=True)
    model_no = fields.Char(string="Model Number", tracking=True)
    warranty_start = fields.Date(string="Warranty Start Date" , tracking=True)
    warranty_end = fields.Date(string="Warranty End Date" , tracking=True)
    partner_id = fields.Many2one('res.partner', string="Customer", required=True, tracking=True)
    active = fields.Boolean(default=True)

    @api.constrains('warranty_start', 'warranty_end')
    def _constrains_warranty_date(self):
        for record in self:
            if record.warranty_start and record.warranty_end and record.warranty_start > record.warranty_end:
                raise ValidationError(_('Warranty end date cannot be earlier than the warranty start date.'))

    @api.constrains('indoor_model_sr', 'outdoor_model_sr')
    def _check_unique_serial_numbers(self):
        print("_____________serial_number__________",self)
        for record in self:
            if record.indoor_model_sr:
                existing_indoor = self.search([
                    ('id', '!=', record.id),
                    ('indoor_model_sr', '=', record.indoor_model_sr)
                ])
                if existing_indoor:
                    raise ValidationError(_('The Indoor Model Serial Number "%s" is already in use.') % record.indoor_model_sr)

            if record.outdoor_model_sr:
                existing_outdoor = self.search([
                    ('id', '!=', record.id),
                    ('outdoor_model_sr', '=', record.outdoor_model_sr)
                ])
                if existing_outdoor:
                    raise ValidationError(_('The Outdoor Model Serial Number "%s" is already in use.') % record.outdoor_model_sr)
