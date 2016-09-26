#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_reference_phrase(models.Model):
    _name = 'setting.reference.phrase'

    phrasecode = fields.Char('片語代號')
    phrasename = fields.Char('片語名稱')