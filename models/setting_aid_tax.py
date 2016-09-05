#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_aid_tax(models.Model):
    _name = 'setting.aid.tax'
    #基本資料
    pyrecedcap = fields.Integer(string="上年度已收資本")
    tyrecedcap = fields.Integer(string="本年度已收資本")  #此欄位格式需要修改
    divintratio = fields.Float(string="股息、年息比率%")
    cashcapincre = fields.Integer(string="現金增資")
    hrcapincre = fields.Integer(string="行使認股權轉增資")
    etdnonslwcls = fields.Integer(string="非緩課")  #"盈餘或員工紅利轉增資"
    etdslwcls = fields.Integer(string="緩課")  #"盈餘或員工紅利轉增資"
    nescucapincre = fields.Integer(string="有價證券轉增資")
    othercapincre = fields.Integer(string="其他轉增資")
    tycapdecre = fields.Integer(string="本年度減資金額")
    regshodiv = fields.Float(string="股東紅利%")  #章程訂定-%
    regdireward = fields.Float(string="董監酬勞%")  #章程訂定-%
    regstafdiv = fields.Float(string="員工紅利%")  #章程訂定-%
    leglsupcapincre = fields.Integer(string="法定公積轉增資")
    capsupcapincre = fields.Integer(string="資本公積轉增資")
    techpricapincre = fields.Integer(string="技術作價轉增資")
    elrightdate = fields.Date(string="除權基準日")
    elintdate = fields.Date(string="除息基準日")
    curvalue = fields.Integer(string="每股面額")
    distredyarn = fields.Integer(string="已發行股數")
    shmetbclsprc = fields.Integer(string="股東會前一天收盤價")
    shdtaxratlaw = fields.Selection([('1','1'),('2','2')],'股東可扣抵稅額比率求法(獲配股利淨額總計*稅額扣抵比率)')
    leglsupris = fields.Float(string="法定公積提列%")
    incapextplaname = fields.Char(string="擴建計畫名稱")  #增資緩課核備資料
    incapapdate = fields.Date(string="核准日期")  #增資緩課核備資料
    incapapnum = fields.Char(string="核准文號")  #增資緩課核備資料
    incapestfshday = fields.Date(string="預計完成日")  #增資緩課核備資料



