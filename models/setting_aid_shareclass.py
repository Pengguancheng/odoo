# coding=utf-8
from openerp import models, fields, api

class setting_aid_shareclass(models.Model):
    _name = 'setting.aid.shareclass'
    #維護
    classnum = fields.Char(string="類別代號")  #可用英數編號，最多可輸入四碼
    entclass = fields.Char(string="分錄類別")  #依據螢幕指示輸入類別代號，例：〔10〕表進貨時使用之分錄，〔20〕表銷貨時使用之分錄．．．等
    debtrassub = fields.Char(string="借方交易科目")  #按"註"開啟“會計科目檔”查詢
    debabcls = fields.Char(string="借方摘要類別")  #依畫面提示輸入借方摘要存放內容，選擇〔4_自行輸入〕時，才可輸入〔借方摘要內容〕。
    debabcont = fields.Char(string="借方摘要內容")
    credtrassub = fields.Char(string="貸方交易科目")  #按"註"開啟“會計科目檔”查詢
    credabcls = fields.Char(string="貸方摘要類別")  #依畫面提示輸入貸方摘要存放內容，選擇〔4_自行輸入〕時，才可輸入〔借方摘要內容〕。
    credabcont = fields.Char(string="貸方摘要內容")
    taxamsub = fields.Char(string="稅額科目")  #輸入進／銷項稅額的會計科目代號，可按註開啟“會計科目檔”查詢
    taxamabcls = fields.Char(string="稅額摘要類別")  #依畫面提示輸入稅額科目摘要存放內容，選擇〔4_自行輸入〕時，才可輸入〔稅額摘要內容〕
    taxamabcont = fields.Char(string="稅額摘要內容")
