from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.category'

    part_code_ids = fields.Many2many(
        'your_module_name.part.code',
        'product_category_part_code_rel',
        'category_id',
        'part_code_id',
        string='Part Codes',
    )
