from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users' 

    prod_commission_ids = fields.One2many("product.commission", "user_id", string="Product Commissions")
    product_id = fields.Many2one("product.product", string="Product", required=True)
    comm_fixed = fields.Float(string="Commission Fixed")
    comm_percent = fields.Float(string="Commission %")
    incentive_amount = fields.Char(string="Incentive")
    no_of_call = fields.Char(string="No Of Call")
    