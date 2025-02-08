from odoo import models, fields, api, _
from datetime import date

class AssetBrand(models.Model):
    _name = 'asset.brand'
    _description = 'AC Service'
    
    name = fields.Char(string="Brand", required=True)
    active = fields.Boolean(default=True)
