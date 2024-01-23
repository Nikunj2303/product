from odoo import models, fields, api

class ImportProducts(models.Model):
    _name = 'import.products'

    upload_file = fields.Binary(string='Upload File')
    filename = fields.Char(string='Filename')
    process = fields.Selection([('import_products', 'Import Products')], string='Process', default='import_products')

    def process_button(self):
        imported_data = self.import_data()
        excel_data = self.read_excel_data()
        data_dict = self.convert_to_dict(imported_data, excel_data)
        print(data_dict)
        return True


