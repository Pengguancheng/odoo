#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_aid_tax(models.Model):
    _name = 'setting.reference.standerdclass'

    subject = fields.Selection([('1','1-證期會科目'),('2','2-結算科目'),('1','2-文中標準板')],'科目別')
    classcode = fields.Char('類別代號')
    entrycate = fields.Selection([('10','10-進貨'),('20','20-銷貨')],'分錄類別')
    debittran = fields.Char('借方交易科目')
    debitclass = fields.Selection([('1','發票號碼'),('4','自行輸入')],'借方摘要類別')
    debitcont = fields.Char('借方摘要內容')  #選擇4-自行輸入才可填寫
    credittran = fields.Char('貸方交易科目')
    creditclass = fields.Selection([('1','發票號碼'),('4','自行輸入')],'貸方摘要類別')
    creditcont = fields.Char('貸方摘要內容')  #選擇4-自行輸入才可填寫
    taxsubject = fields.Char('稅額科目')
    taxclass = fields.Selection([('1','發票號碼'),('4','自行輸入')],'稅額摘要類別')
    taxcont = fields.Char('稅額摘要內容')