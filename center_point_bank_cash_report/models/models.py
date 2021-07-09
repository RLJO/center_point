# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class NewAccountMove(models.Model):
    _inherit = 'account.move'

    entry_sq_code = fields.Char(string="Code", required=False)
    entry_title = fields.Char(compute='create_sequence')
    cp_title = fields.Char(compute='create_sequence')


    @api.depends('journal_id')
    def create_sequence(self):
        var = ''
        cp_title = ''
        payment = self.payment_id
        statement = self.statement_line_id
        if self.journal_id.type == 'cash':
            # Use the right sequence to set the sq_code
            if payment:
                if payment.partner_type == 'customer':
                    if payment.payment_type == 'inbound':
                        var = 'قبض نقدى'
                        cp_title = 'إستلمنا من'
                    if payment.payment_type == 'outbound':
                        var = 'صرف نقدى'
                        cp_title = 'إستلمت أنا'

                if payment.partner_type == 'supplier':
                    if payment.payment_type == 'inbound':
                        var = 'قبض نقدى'
                        cp_title = 'إستلمنا من'
                    if payment.payment_type == 'outbound':
                        var = 'صرف نقدى'
                        cp_title = 'إستلمت أنا'
            if statement:
                if statement.amount > 0.0:
                    var = 'قبض نقدى'
                    cp_title = 'إستلمنا من'
                else:
                    var = 'صرف نقدى'
                    cp_title = 'إستلمت أنا'

        self.entry_title = var
        self.cp_title = cp_title


class NewAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    text_amount = fields.Char(string="Amount in letters", required=False, compute="amount_to_text")

    cant_edit = fields.Boolean(compute="_compute_can_edit")

    @api.depends('move_id.purchase_id', 'move_id.invoice_user_id')
    def _compute_can_edit(self):
        for rec in self:
            print(rec.purchase_order_id)
            print(rec.sale_line_ids)
            if rec.purchase_order_id or rec.sale_line_ids:
                rec.cant_edit = True
            else:
                rec.cant_edit = False
            print(rec.cant_edit)


    # @api.multi
    @api.depends('balance')
    def amount_to_text(self):
        for line in self:
            lang = self.env.user.lang
            print(lang)
            line.text_amount = num2words(abs(line.balance), lang='ar_001')


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

            self.move_id.entry_sq_code = self.env['ir.sequence'].next_by_code(sequence_code, sequence_date=self.date)
            self.move_id._post(soft=False)


class NewAccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    def button_post(self):
        ''' Move the bank statements from 'draft' to 'posted'. '''
        if any(statement.state != 'open' for statement in self):
            raise UserError(_("Only new statements can be posted."))

        self._check_balance_end_real_same_as_computed()

        for statement in self:
            if not statement.name:
                statement._set_next_sequence()

        self.write({'state': 'posted'})
        lines_of_moves_to_post = self.line_ids.filtered(lambda line: line.move_id.state != 'posted')
        if lines_of_moves_to_post:
            for line in lines_of_moves_to_post:
                if line.amount > 0.0:
                    sequence_code = 'account.payment.customer.invoice'
                else:
                    sequence_code = 'account.payment.supplier.invoice'

                line.move_id._post(soft=False)
                line.move_id.entry_sq_code = self.env['ir.sequence'].next_by_code(sequence_code,
                                                                                                sequence_date=self.date)
