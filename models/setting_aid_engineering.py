#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_aid_engineering(models.Model):
    _name = 'setting.aid.engineering'
    #基本資料
    egnid = fields.Char('工程編號')
    egnsname = fields.Char('工程簡稱')
    egnname = fields.Char('工程名稱')
    egnlocation = fields.Char('工程地點')
    cid = fields.Char('業主代號')
    address = fields.Char('座落地號')
    organizer = fields.Char('主辦機關')
    dealdate = fields.Date('合約日期')
    dealend = fields.Date('約定完工')
    realstart = fields.Date('實際開工')
    realend = fields.Date('實際完工', readonly=True)
    chkdate = fields.Date('驗收日期')
    startdate = fields.Date('施工期間(起)')
    enddate = fields.Date('施工期間(迄)')
    costmeth = fields.Selection([('1','全部完工'),('0','完工比例')],'成本法')
    earlywork = fields.Float('前期完工度', readonly=True)
    nowwork = fields.Float('本期完工度', readonly=True)
    tag = fields.Char('備註')
    sitemoneystanderd = fields.Float('工地金額分攤基準')
    coststanderd = fields.Float('成本費用分攤基準')
    costrate = fields.Float('成本費用分攤比率')
    delayrate = fields.Float('遞延費用轉列比例')
    #收入費用
    dealm = fields.Integer('合約金額')
    discountm = fields.Integer('-折讓金額')
    earlyaddm = fields.Integer('+前期追加')
    nowaddm = fields.Integer('+本期追加')
    chkm = fields.Integer(string='=驗收金額', compute='_chkm_onchange')
    chkmr = fields.Integer('驗收金額')
    advanceme = fields.Integer('前期預收金額', readonly=True)
    advancemn = fields.Integer('本期預收金額', readonly=True)
    incomeme = fields.Integer('前期收入金額', readonly=True)
    incomemn = fields.Integer('本期收入金額', readonly=True)
    grossme = fields.Integer('前期毛利金額', readonly=True)
    grossmn = fields.Integer('本期毛利金額', readonly=True)
    count1 = fields.Integer('合約金額-收入金額', readonly=True)
    count2 = fields.Integer('驗收金額-收入金額', readonly=True)
    #工程費用
    #材料
    material_e = fields.Integer('材料前期費用', readonly=True)
    material_n = fields.Integer('材料本期費用', readonly=True)
    material_r = fields.Integer('材料實際費用', readonly=True)
    material_b = fields.Integer('材料預算費用')
    #工程費用
    engineering_e = fields.Integer('工程前期費用', readonly=True)
    engineering_n = fields.Integer('工程本期費用', readonly=True)
    engineering_r = fields.Integer('工程實際費用', readonly=True)
    engineering_b = fields.Integer('工程預算費用')
    #人工費用
    people_e = fields.Integer('人工前期費用', readonly=True)
    people_n = fields.Integer('人工本期費用', readonly=True)
    people_r = fields.Integer('人工實際費用', readonly=True)
    people_b = fields.Integer('人工預算費用')
    #外包費用
    Outsourcing_e = fields.Integer('外包前期費用', readonly=True)
    Outsourcing_n = fields.Integer('外包本期費用', readonly=True)
    Outsourcing_r = fields.Integer('外包實際費用', readonly=True)
    Outsourcing_b = fields.Integer('外包預算費用')
    #合計
    total_e = fields.Integer('合計前期費用', readonly=True)
    total_n = fields.Integer('合計本期費用', readonly=True)
    total_r = fields.Integer('合計實際費用', readonly=True)
    total_b = fields.Integer('合計預算費用', readonly=True)
    #建物
    householdnum = fields.Integer('總戶數')
    parkingnum = fields.Integer('車位數')
    hassessment = fields.Selection([('1','收入法'),('2','建坪比例法'),('3','建屋方式')],'房屋估價方法')
    constructionm = fields.Selection([('0','自地自建'),('1','合建分屋'),('2','合建分售'),('3','合建分成'),('4','共同投資興建')],'建屋方式')
    landcost = fields.Integer('土地總成本')
    landarea = fields.Integer('/土地面積')
    landgcost = fields.Integer('=每坪成本')
    landgarea = fields.Integer('/面積（㎡）')
    m2cost = fields.Integer('=每㎡成本')
    housetcost = fields.Integer('房屋總成本')
    floorspace = fields.Integer('/總建坪')
    spacecost = fields.Integer('=每坪成本')
    m2space = fields.Integer('/面積（㎡）')
    m2spacecost = fields.Integer('=每㎡成本')\

    @api.onchange('dealm','discountm','earlyaddm','nowaddm')
    def _chkm_onchange(self):
        self.chkm = self.dealm - self.discountm +self.earlyaddm +self.nowaddm
        self.chkmr = self.chkm
    @api.onchange('landcost','landarea')
    def _land_change1(self):
        self.landgcost = self.landcost / self.landarea
    @api.onchange('landcost','landgarea')
    def _land_change(self):
        self.m2cost = self.landcost / self.landgarea
    @api.onchange('housetcost','floorspace')
    def _house_change(self):
        self.spacecost = self.housetcost / self.floorspace
    @api.onchange('housetcost','m2space')
    def _house_change1(self):
        self.m2spacecost = self.housetcost / self.m2space