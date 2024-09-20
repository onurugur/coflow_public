from odoo import models, fields, api, _


class update_discount(models.TransientModel):
    _name = 'update.discount'
    _description="Update Discount"

    @api.model
    def default_get(self, fields):
        res = super(update_discount, self).default_get(fields)
        context = dict(self._context)
        active_id = context.get('active_id')
        so_line_rec = self.env['sale.order.line'].browse(active_id)
        if so_line_rec.unit_discounted:
            res.update({'unit_discounted': so_line_rec.unit_discounted,
                        'price_unit': so_line_rec.price_unit})
        return res

    unit_discounted = fields.Float('Discount Price',
                                  digits='Product Price')
    price_unit = fields.Float('Unit Price',
                                  digits='Product Price')

    def update_discount_price(self):
        context = dict(self._context)
        active_id = context.get('active_id')
        so_line_rec = self.env['sale.order.line'].browse(active_id)
        so_line_rec.write({'discount': ( 100.0 - (100.0 * (self.unit_discounted / self.price_unit)))})
        return True

class UpdateDisconunt(models.TransientModel):
    _name = 'invoice.update.discount'
    _description="Update Discount"

    @api.model
    def default_get(self, fields):
        res = super(UpdateDisconunt, self).default_get(fields)
        context = dict(self._context)
        active_id = context.get('active_id')
        so_line_rec = self.env['account.move.line'].browse(active_id)
        if so_line_rec.unit_discounted:
            res.update({'unit_discounted': so_line_rec.unit_discounted,
                        'price_unit': so_line_rec.price_unit})
        return res

    unit_discounted = fields.Float('Discount Price',
                                  digits='Product Price')
    price_unit = fields.Float('Unit Price',
                                  digits='Product Price')

    def update_discount_price(self):
        context = dict(self._context)
        active_id = context.get('active_id')
        so_line_rec = self.env['account.move.line'].browse(active_id)
        so_line_rec.write({'discount': ( 100.0 - (100.0 * (self.unit_discounted / self.price_unit)))})
        return True
