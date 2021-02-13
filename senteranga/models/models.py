# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, RedirectWarning, UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    @api.depends('list_price', 'standard_price')
    def _compute_marge(self):
        marge = 0
        for record in self:
            marge = record.list_price - record.standard_price
            record.marge = marge if marge > 0 else 0 
    
    list_price = fields.Float(
        'Sales Price', default=1.0,
        digits='Product Price', required=True,
        help="Price at which the product is sold to customers.")
    standard_price = fields.Float(
        'Cost', compute='_compute_standard_price', required=True,
        inverse='_set_standard_price', search='_search_standard_price',
        digits='Product Price', groups="base.group_user",
        help="""In Standard Price & AVCO: value of the product (automatically computed in AVCO).
        In FIFO: value of the last unit that left the stock (automatically computed).
        Used to value the product when the purchase cost is not known (e.g. inventory adjustment).
        Used to compute margins on sale orders.""")
    barcode = fields.Char(
        'Barcode', compute='_compute_barcode', required=True,
        inverse='_set_barcode', search='_search_barcode')
    seller_ids = fields.One2many(
        'product.supplierinfo', 'product_tmpl_id', 
        required=True, string='Vendors', 
        help="Define vendor pricelists.")
    marge = fields.Float('Marge', compute='_compute_marge')
    
    @api.model
    def create(self, vals):
        if not vals.get('seller_ids'):
            raise UserError(_('Vous devez ajouter un fournisseur. '))
        if vals.get('standard_price') <= 0:
            raise UserError(_('Vous devez renseigner le coût.'))
        if vals.get('list_price') <= 0:
            raise UserError(_('Vous devez renseigner le prix de vente.'))
        return super(ProductTemplate, self).create(vals)
    
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if not self.seller_ids:
            raise UserError(_('Vous devez ajouter un fournisseur. '))
        if self.standard_price <= 0:
            raise UserError(_('Vous devez renseigner le coût.'))
        if self.list_price <= 0:
            raise UserError(_('Vous devez renseigner le prix de vente.'))
        return res


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    payment_term_id = fields.Many2one(
        'account.payment.term', string='Payment Terms', required=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
