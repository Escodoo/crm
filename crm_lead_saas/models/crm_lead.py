# Copyright 2021 - TODAY, Marcel Savegnago <marcel.savegnago@escodoo.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):

    _inherit = 'crm.lead'

    amount_mrr = fields.Monetary(
        'Amount MRR',
        currency_field='company_currency',
        track_visibility='always',
        help='Amount Monthly Recurring Revenue')

    amount_arr = fields.Monetary(
        'Amount ARR',
        currency_field='company_currency',
        track_visibility='always',
        help='Amount Anual Recurring Revenue')

    amount_nrr = fields.Monetary(
        'Amount NRR',
        currency_field='company_currency',
        track_visibility='always',
        help='Amount Non-Recurring Revenue')

    def _compute_amount_arr(self):
        for rec in self:
            if rec.amount_mrr:
                rec.amount_arr = rec.amount_mrr * 12

    @api.onchange('amount_mrr')
    def _onchange_amount_mrr(self):
        for rec in self:
            rec._compute_amount_arr()
