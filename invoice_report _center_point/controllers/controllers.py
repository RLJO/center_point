# -*- coding: utf-8 -*-
from odoo import http

# class Repooo/pro(http.Controller):
#     @http.route('/repooo/pro/repooo/pro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/repooo/pro/repooo/pro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('repooo/pro.listing', {
#             'root': '/repooo/pro/repooo/pro',
#             'objects': http.request.env['repooo/pro.repooo/pro'].search([]),
#         })

#     @http.route('/repooo/pro/repooo/pro/objects/<model("repooo/pro.repooo/pro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('repooo/pro.object', {
#             'object': obj
#         })