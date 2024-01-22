from odoo import models, fields

class ProductsImportHistory(models.Model):
    _name = 'products.import.history'
    _description = 'Products Import History'

    product_template_id = fields.Many2one('product.template', string='Product Template')
    partner_id = fields.Many2one('res.partner', string='Partner')
    old_price = fields.Float(string='Old Price')
    new_price = fields.Float(string='New Price')
