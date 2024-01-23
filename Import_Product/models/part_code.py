from odoo import models, fields

class PartCode(models.Model):
    _name = 'part.code'
    _description = 'Part Code'

    part_no = fields.Char(string='Part No')
    description = fields.Char(string='Description')
