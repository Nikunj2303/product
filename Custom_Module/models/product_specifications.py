from odoo import models, fields

from odoo import models, fields

class ProductSpecification(models.Model):
    _name = 'product.specification'
    _description = 'Product Specification'

    SPEC_CHOICES = [
        ('is_case', 'Is Case'),
        ('is_dial', 'Is Dial'),
        ('is_bracelet', 'Is Bracelet'),
        ('is_caliber', 'Is Caliber'),
    ]

    part_selection = fields.Selection(
        SPEC_CHOICES,
        string='Specification',
        required=True
    )

    starting_caliber_char = fields.Char(
        string='Starting Char',
        help='This field is visible only when Is Caliber is selected on Specification.'
    )

    part_code_ids = fields.Many2many(
        'part.code',
        string='Part Codes'
    )

    search_terms_ids = fields.Many2many(
        'search.term',
        string='Searching Terms'
    )

