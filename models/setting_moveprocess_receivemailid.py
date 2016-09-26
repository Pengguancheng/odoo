#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_moveprocess_receivemailid(models.Model):
    _name = 'setting.moveprocess.receivemailid'

    billrecivnum = fields.Boolean('結算收件編號')
    temporpaynum = fields.Boolean('暫繳收件編號')
    billtempor = fields.Boolean('結算及暫繳收件編號')
    earndistratio = fields.Boolean('盈餘分配比率')
    notefinote = fields.Boolean('申報書附件註記')