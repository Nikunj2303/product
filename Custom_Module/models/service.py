from odoo import api,fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    vendor_id = fields.Many2one('res.partner', string='Vendor')
    currency_id = fields.Many2one('res.currency', string='Currency')
    product_category_id = fields.Many2one('product.category', string='Product Category')

