#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_reference_certificate(models.Model):
    _name = 'setting.reference.certificate'

    certifikind = fields.Char('憑證種類')
    certificont = fields.Char('憑證說明')