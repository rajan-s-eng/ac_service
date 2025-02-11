from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users' 

    prod_commission_ids = fields.One2many("product.commission", "user_id", string="Product Commissions")
