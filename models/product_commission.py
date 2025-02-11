from odoo import fields, models


class ProductCommission(models.Model):
    _name = 'product.commission'
    _description = 'AC Service'
    _rec_name = "product_id"

    product_id = fields.Many2one("product.product", string="Product", required=True)
    comm_fixed = fields.Float(string="Commission Fixed")
    comm_percent = fields.Float(string="Commission %")
    user_id = fields.Many2one('res.users', string="Technician", required=True)
    incentive_amount = fields.Char(string="Incentive")
    no_of_call = fields.Char(string="No Of Call")
