from odoo import models, fields, api, _
from datetime import date

class ProductCommission(models.Model):
    _name = 'product.commission'
    _description = 'AC Service'
    _rec_name = "product_id"

    product_id = fields.Many2one("product.product", string="Product" ,required=True)
    comm_fixed = fields.Float(string="Commission Fixed")
    comm_percent = fields.Float(string="Commission %")
    user_id = fields.Many2one('res.users', string="Technician")
