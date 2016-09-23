#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_reference_propertysign(models.Model):
    _name = 'setting.reference.propertysign'

    accountcode = fields.Char('財簽科目代號')
    accountname = fields.Char('財簽科目名稱')
    lend = fields.Selection([('0','借'),('1','貸')],'借/貸')