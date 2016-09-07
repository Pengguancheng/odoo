# coding=utf-8
from openerp import models, fields, api

class setting_aid_customer(models.Model):
    _name = 'setting.aid.relate'
    #其他、營業稅
        #(其他科目)
    cash = fields.Integer(string="現金")
    recietick = fields.Integer(string="應收票據")
    paytick = fields.Integer(string="應付票據")
    reciecredit = fields.Integer(string="應收帳款")
    paycredit = fields.Integer(string="應付帳款")
    inctaxam = fields.Integer(string="進項稅額")
    selltaxam = fields.Integer(string="銷項稅額")
    selproptgain = fields.Integer(string="出售資產增益")
    selproptloss = fields.Integer(string="出售資產損失")
    oincome = fields.Integer(string="其他收入")
    othloss = fields.Integer(string="其他損失")
        #(營業稅)
    paytaxam = fields.Integer(string="應納稅額")
    remtaxam = fields.Integer(string="留抵稅額")
    btaxam = fields.Integer(string="應退稅額")
    restbtaxam = fields.Integer(string="歇業(調整)應退稅額")
    impaytaxam = fields.Integer(string="進口貨物應納稅額科目")
    purospaytaxam = fields.Integer(string="購買國外勞務應納稅額")
    stpaytaxam = fields.Integer(string="特種稅額應納稅額科目")
    mdpaytaxam = fields.Integer(string="補徵應繳稅額科目")
    # 工程/建物成本
        #在建工程科目
    ineconsumtrl = fields.Integer(string="耗用材料")  #欄位需調整
    inederimannu = fields.Integer(string="直接人工")  #欄位需調整
    ineoutsourcf = fields.Integer(string="外包費用")  #欄位需調整
    inenginrstartf = fields.Integer(string="工程費用(起)")  #欄位需調整
    inenginrendf = fields.Integer(string="工程費用(訖)")  #欄位需調整
    ineadvsengnrf = fields.Integer(string="預收工程款")
        #其他科目
    otaccengnrf = fields.Integer(string="應收工程款")
    otadvsengnrf = fields.Integer(string="預收工程款")
    otengnrproflos = fields.Integer(string="工程損益科目")
    otengnrproincm = fields.Integer(string="工程收入科目")
    otengnrprocost = fields.Integer(string="工程成本科目")
    otrealintre = fields.Integer(string="在建工程-已實現利益")
        #建物科目
    bsbiuldplace = fields.Integer(string="營建用地")
    bs4selland = fields.Integer(string="待售土地")
    bsinbilplace = fields.Integer(string="在建房地")
    bs4selhouse = fields.Integer(string="代售房屋")