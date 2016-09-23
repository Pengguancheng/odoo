#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_reference_taxoffical(models.Model):
    _name = 'setting.reference.taxoffical'

    taxauthoritycode = fields.Char('國稅稽徵機關代號')
    taxauthorityname = fields.Char('國稅稽徵機關名稱')