
from odoo import models, fields

class SearchTerm(models.Model):
    _name = 'search.term'
    _description = 'Searching Term'

    search_term = fields.Char(
        string='Searching Term',
        required=True
    )
