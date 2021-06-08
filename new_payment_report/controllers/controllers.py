# -*- coding: utf-8 -*-
# from odoo import http


# class NewPaymentReport(http.Controller):
#     @http.route('/new_payment_report/new_payment_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_payment_report/new_payment_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_payment_report.listing', {
#             'root': '/new_payment_report/new_payment_report',
#             'objects': http.request.env['new_payment_report.new_payment_report'].search([]),
#         })

#     @http.route('/new_payment_report/new_payment_report/objects/<model("new_payment_report.new_payment_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_payment_report.object', {
#             'object': obj
#         })
