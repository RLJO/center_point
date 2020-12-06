from odoo import api, fields, models

class centerpoint(models.Model):
    _inherit = 'project.project'

    parent_project = fields.Many2one(comodel_name="project.project", string="Parent Project", required=False, )


class insurance(models.Model):
    _inherit = 'account.move'

    contracting_insurance = fields.Boolean(string="Contracting Insurance")
class NewModule(models.Model):
    _inherit = 'account.move.line'

    contracting_insurance_ham = fields.Boolean(string="Contracting Insurance")
