# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class NewAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    text_amount = fields.Char(string="Amount in letters", required=False, compute="amount_to_text")

    # @api.multi
    @api.depends('debit', 'credit')
    def amount_to_text(self):
        if self.debit > 0.0:
            self.text_amount = self.currency_id.amount_to_text(self.debit)

        if self.credit > 0.0:
            self.text_amount = self.currency_id.amount_to_text(self.debit)


class NewAccountPayment(models.Model):
    _inherit = 'account.payment'

    text_amount = fields.Char(string="Amount in letters", required=False, compute="amount_to_text")
    sq_code = fields.Char(string="Code", required=False)

    # @api.multi
    @api.depends('amount')
    def amount_to_text(self):
        print('t')
        self.text_amount = self.currency_id.amount_to_text(self.amount)

    def action_post(self):
        self.move_id._post(soft=False)
        ''' draft -> posted '''
        global sequence_code
        i = 0
        if not self.sq_code:
            # Use the right sequence to set the sq_code
            if self.partner_type == 'customer':
                if self.payment_type == 'inbound':
                    sequence_code = 'account.payment.customer.invoice'
                if self.payment_type == 'outbound':
                    sequence_code = 'account.payment.customer.refund'
            if self.partner_type == 'supplier':
                if self.payment_type == 'inbound':
                    sequence_code = 'account.payment.supplier.refund'
                if self.payment_type == 'outbound':
                    sequence_code = 'account.payment.supplier.invoice'

            print(sequence_code)
            print(i)
            self.sq_code = self.env['ir.sequence'].next_by_code(sequence_code, sequence_date=self.date)
            print(self.sq_code)
            # if not self.sq_code:
            #     raise UserError(_("You have to define a sequence for %s in your company.") % (sequence_code,))
