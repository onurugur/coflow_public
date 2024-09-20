# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    unit_discounted = fields.Float('Disc. Unit',
                                   digits='Product Price',
                                   compute='_compute_unit_discounted',
                                   readonly=True,
                                   store=True)

    @api.depends('price_unit', 'discount')
    def _compute_unit_discounted(self):
        for sl in self:
            sl.unit_discounted = sl.price_unit * ((100.0 -sl.discount) / 100.0)

    def _prepare_invoice_line(self, **optional_values):
        """
            If the sale order line isn't linked to a sale order which already have a default analytic account,
            this method allows to retrieve the analytic account which is linked to project or task directly linked
            to this sale order line, or the analytic account of the project which uses this sale order line, if it exists.
        """
        values = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        values['unit_discounted']=self.unit_discounted
        return values

class AccountMoveLine(models.Model):
    _inherit='account.move.line'

    unit_discounted = fields.Float('Disc. Unit',
                                   digits='Product Price',
                                   compute='_compute_unit_discounted',
                                   readonly=True,
                                   store=True)

    @api.depends('price_unit', 'discount')
    def _compute_unit_discounted(self):
        for sl in self:
            sl.unit_discounted = sl.price_unit * ((100.0 - sl.discount) / 100.0)



