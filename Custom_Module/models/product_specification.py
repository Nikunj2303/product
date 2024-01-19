from odoo import models, fields

class ProductSpecifications(models.Model):
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
        string='Specifications',
        required=True,
    )

    starting_caliber_char = fields.Char(
        string='Starting Char',
        invisible="{'part_selection': [('=', 'is_caliber')]}",
    )

    part_code_ids = fields.Many2many(
        'part.code',
        string='Part Codes',
    )

    search_terms_ids = fields.Many2many(
        'search.term',
        string='Searching Terms',
    )
