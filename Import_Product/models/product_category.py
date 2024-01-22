from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = "product.category"

    part_code_ids = fields.Many2many('product.category.part.code', string='Part Codes')
