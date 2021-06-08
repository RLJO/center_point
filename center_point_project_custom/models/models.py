# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class center_point_project_custom(models.Model):
#     _name = 'center_point_project_custom.center_point_project_custom'
#     _description = 'center_point_project_custom.center_point_project_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
