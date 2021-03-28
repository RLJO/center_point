from odoo import api, fields, models


class NewModule(models.Model):
    _name = 'invoice.report'


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def create_sales_order(self):
        for rec in self:
            approv = self.env['approval.request'].create({
                'request_owner_id':rec.partner_id,

            })



class NewModule(models.Model):
    _inherit = 'account.payment'




