#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_reference_bank(models.Model):
    _name = 'setting.reference.bank'

    bankcode = fields.Char('銀行代號')
    bankacroname = fields.Char('銀行簡稱')
    bankfullname = fields.Char('銀行全稱')