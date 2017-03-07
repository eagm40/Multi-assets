from odoo import api, fields, models
from odoo.tools import float_compare, float_is_zero, DEFAULT_SERVER_DATE_FORMAT as DF
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError, ValidationError

class AccountAssetCategory(models.Model):
    _inherit = 'account.asset.category'

    asset_detail = fields.Boolean(string='Ingresar Activos Multiples', store=True, default=False, traslate=True)