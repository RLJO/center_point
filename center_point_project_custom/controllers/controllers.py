# -*- coding: utf-8 -*-
# from odoo import http


# class CenterPointProjectCustom(http.Controller):
#     @http.route('/center_point_project_custom/center_point_project_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/center_point_project_custom/center_point_project_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('center_point_project_custom.listing', {
#             'root': '/center_point_project_custom/center_point_project_custom',
#             'objects': http.request.env['center_point_project_custom.center_point_project_custom'].search([]),
#         })

#     @http.route('/center_point_project_custom/center_point_project_custom/objects/<model("center_point_project_custom.center_point_project_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('center_point_project_custom.object', {
#             'object': obj
#         })
