# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    chield_tasks_count = fields.Integer(compute='_compute_chield_tasks_count')

    # @api.depends('id')
    def _compute_chield_tasks_count(self):
        chield_projects = self.env['project.project'].search([('parent_project', '=', self.id)])
        print('chield projects = ', len(chield_projects))
        count = 0
        for chield in chield_projects:
            count += chield.task_count

        self.chield_tasks_count = count
        print('count = ', count)
        print('chield_tasks_count = ', self.chield_tasks_count)




