from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_case = fields.Boolean(string='Is Case', default=False)
    is_dial = fields.Boolean(string='Is Dial', default=False)
    is_bracelet = fields.Boolean(string='Is Bracelet', default=False)
    is_caliber = fields.Boolean(string='Is Caliber', default=False)
