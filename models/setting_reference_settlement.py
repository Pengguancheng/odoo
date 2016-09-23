#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_reference_settlement(models.Model):
    _name = 'setting.reference.settlement'

    accountcode = fields.Char('結算科目代號')
    accountname = fields.Char('結算科目名稱')
    lend = fields.Selection([('0','借'),('1','貸')],'借/貸')