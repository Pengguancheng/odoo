#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_reference_taxoffical(models.Model):
    _name = 'setting.reference.taxoffical'

    accountcode = fields.Char('科目代號')
    accountname = fields.Char('科目名稱')
    lend = fields.Selection([],'借/貸')