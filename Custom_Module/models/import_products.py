from odoo import models, fields


class ImportProducts(models.Model):
    _name = 'import.products'

    upload_file = fields.Binary(string='Upload File')
    filename = fields.Char(string='Filename')
    process = fields.Selection([('import_products', 'Import Products')], string='Process', default='import_products')

    def process_button(self):
        return True