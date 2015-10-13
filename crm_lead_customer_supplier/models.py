# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class Lead(models.Model):
    _inherit = "crm.lead"

    customer = fields.Boolean(
        help="Check this box if this contact is a customer.")
    supplier = fields.Boolean(
        help="Check this box if this contact is a supplier.")

    @api.model
    def _lead_create_contact(self, lead, name, is_company, parent_id=False):
        """Add fields to partner."""
        ctx = {
            "default_customer": lead.customer,
            "default_supplier": lead.supplier,
        }
        return (super(Lead, self.with_context(**ctx))
                ._lead_create_contact(lead, name, is_company, parent_id))

    def on_change_partner_id(self, partner_id):
        """Recover customer and supplier from partner if available."""
        result = super(Lead, self).on_change_partner_id(partner_id)

        if result.get("value"):
            if self.partner_id:
                result["value"]["customer"] = self.partner_id.customer
                result["value"]["supplier"] = self.partner_id.supplier

        return result
