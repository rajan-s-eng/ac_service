from odoo import models, fields, api, _
from datetime import date

class PartnerAsset(models.Model):
    _name = 'partner.asset'
    _description = 'AC Service'

    name = fields.Char(string="Product", required=True)
    invoice_no = fields.Char(string="Invoice Number")
    brand_id = fields.Many2one('asset.brand', string="Brand", required=True)
    model_no = fields.Char(string="Model Number")
    warranty_start = fields.Date(string="Warranty Start Date")
    warranty_end = fields.Date(string="Warranty End Date")
    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    active = fields.Boolean(default=True)
