from odoo import models, fields, api, _
from datetime import date

class AssetService(models.Model):
    _name = 'asset.service'
    _description = 'AC Service'

    name = fields.Char(string="Product")
    partner_id = fields.Many2one('res.paetner', required=True)
    asset_id = fields.Many2one('partner.asset')
