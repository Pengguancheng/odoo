# coding=utf-8
from openerp import models, fields, api

class setting_aid_supply(models.Model):
    _name = 'setting.aid.supply'
    #內容
    num = fields.Char(string="代號")
    kind = fields.Selection([('0','0'),('1','1'),('2','2')],'類別(0-客戶供應商 1-供應商 2-客戶)')
    abbreviation = fields.Char(string="簡稱")
    unifid = fields.Char(string="統一編號")
    taxnation = fields.Char(string="稅籍")
    personid = fields.Char(string="身份證字號")
    companyname = fields.Char(string="全稱")
    receiptadd = fields.Char(string="發票地址")
    caddress = fields.Char(string="聯絡地址")
    tele = fields.Char(string="聯絡電話")
    prokind = fields.Char(string="行業別")
    faxone = fields.Char(string="傳真一")
    faxtow = fields.Char(string="傳真二")
    faxdacode = fields.Char(string="傳真時加撥區碼")
    note = fields.Char(string="備註")
    mainctname = fields.Char(string="姓名")  #主要聯絡人
    mainctjob = fields.Char(string="職稱")  #主要聯絡人
    maincttel = fields.Char(string="分機")  #主要聯絡人
    mainctcel = fields.Char(string="手機")  #主要聯絡人
    mainctmail = fields.Char(string="Mail")  #主要聯絡人
    agctname = fields.Char(string="姓名")  #代理聯絡人
    agctjob = fields.Char(string="職稱")  #代理聯絡人
    agcttel = fields.Char(string="分機")  #代理聯絡人
    agctcel = fields.Char(string="手機")  #代理聯絡人
    agctmail = fields.Char(string="Mail") #代理聯絡人
    pcpname = fields.Char(string="姓名")  #負責人
    pcpbirth = fields.Integer(string="生日月份")  #負責人
    pcptel = fields.Char(string="分機")  #負責人
    pcpcel = fields.Char(string="手機")  #負責人
    pcpmail = fields.Char(string="Mail")  #負責人
    lastreciev = fields.Integer(string="上期應收")
    lastpay = fields.Integer(string="上期應付")
    noteposi = fields.Char(string="註記欄")
    creatdate = fields.Date(string="建立日期")
    modifydate = fields.Date(string="修改日期")
    updater = fields.Char(string="更新者")


