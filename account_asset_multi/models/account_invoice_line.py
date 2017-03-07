# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import calendar
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.tools import float_compare, float_is_zero, DEFAULT_SERVER_DATE_FORMAT as DF
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError, ValidationError

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.one
    def asset_create(self):
        if self.asset_category_id:
            if self.asset_category_id.asset_detail:
                for i in range(int(self.quantity)):
                    vals = {
                        'name': self.name,
                        'code': self.invoice_id.number or False,
                        'category_id': self.asset_category_id.id,
                        'value': self.price_subtotal_signed/ self.quantity,
                        'partner_id': self.invoice_id.partner_id.id,
                        'company_id': self.invoice_id.company_id.id,
                        'currency_id': self.invoice_id.company_currency_id.id,
                        'date': self.invoice_id.date_invoice,
                        'invoice_id': self.invoice_id.id,
                    }
                    changed_vals = self.env['account.asset.asset'].onchange_category_id_values(vals['category_id'])
                    vals.update(changed_vals['value'])
                    asset = self.env['account.asset.asset'].create(vals)
            else:
                vals = {
                    'name': self.name,
                    'code': self.invoice_id.number or False,
                    'category_id': self.asset_category_id.id,
                    'value': self.price_subtotal_signed + self.invoice_id.total_cost,
                    'partner_id': self.invoice_id.partner_id.id,
                    'company_id': self.invoice_id.company_id.id,
                    'currency_id': self.invoice_id.company_currency_id.id,
                    'date': self.invoice_id.date_invoice,
                    'invoice_id': self.invoice_id.id,
                }
                changed_vals = self.env['account.asset.asset'].onchange_category_id_values(vals['category_id'])
                vals.update(changed_vals['value'])
                asset = self.env['account.asset.asset'].create(vals)
            if self.asset_category_id.open_asset:
                asset.validate()
        return True