# coding=utf-8
from openerp import models, fields, api

class setting_aid_customer(models.TransientModel):
    _name = 'setting.aid.company'
    _inherit = 'res.config.settings'


    #基本資料

    company =fields.Char(string="公司代號")
    companyname = fields.Char(string="公司名稱")
    companysname = fields.Char(string="公司簡稱")
    companyename = fields.Char(string="英文名稱")
    tele = fields.Char(string="電話")
    fox = fields.Char(string="傳真電話")
    caddress = fields.Char(string="聯絡地址")
    address = fields.Char(string="戶籍地址")
    taxid = fields.Char(string="稅籍編號")
    uniteid = fields.Char(string="統一編號")
    principal = fields.Char(string="負責人")
    personid = fields.Char(string="身分證號")
    personidtag = fields.Char(string="證號註記")
    principaladdress = fields.Char(string="地址")#負責人地址
    principalbirth = fields.Char(string="出生日期")#負責人出生日期
    principaltele = fields.Char(string="手機")#負責人手機
    cpersonname = fields.Char(string="聯絡人")
    cpersontele = fields.Char(string="手機-聯絡人")
    accountstart = fields.Date(string="會計期間起始")
    startday = fields.Date(string="開業日")
    enddate = fields.Date(string="註銷日期")
    datayear = fields.Integer(string="資料處理年度")
    accountsource = fields.Char(string="科目來源")
    collectionid = fields.Char(string="稽徵機關")
    collectiontele = fields.Char(string="電話-聯絡人")
    saledutyfreestart = fields.Date(string="開始銷售免稅貨物或勞務日期")
    #相關設定(name=代號 len=長度)
    decimallen = fields.Integer(string="金額小數位數")
    accountlen = fields.Integer(string="帳務金額(整數位)")
    buysellonelen = fields.Integer(string="進銷單價(整數位)")
    buysellonedecimallen = fields.Integer(string="進銷單價小數位數(整數位)")
    buysellnumlen = fields.Integer(string="進銷金額(整數位)")
    buysellquantitylen = fields.Integer(string="進銷數量(整數位)")
    buysellquantitydecimallen = fields.Integer(string="進銷數量小數位數(整數位)")
    subjectnamelen = fields.Integer(string="科目代號長度")
    materialnamelen = fields.Integer(string="材料代號長度")
    constructionsitenamelen = fields.Integer(string="工地代號長度")
    datedisplay = fields.Selection([('taiwan','民國'),('west','西元')],'日期顯示方式')
    subjectlen = fields.Integer(string="科目長度")
    standardlen = fields.Integer(string="品名規格長度")
    housetaxcity = fields.Char(string="縣市")
    housetaxtown = fields.Char(string="鄉鎮")
    housetaxvillage = fields.Char(string="村里")
    housetaxnum = fields.Char(string="流水號")
    managecity = fields.Char(string="縣市")
    managecollection = fields.Char(string="稽徵單位")
    managetown = fields.Char(string="鄉縣市")
    manageservicearea = fields.Char(string="服務區")
    accountreportfooter = fields.Char(string="總帳報表表尾")
    buysellreportfooter = fields.Char(string="進銷報表表尾")
    summonsreportfooter = fields.Char(string="傳票報表表尾")
    companyemail = fields.Char(string="電子郵件信箱")
    #結算設定
    businessclass = fields.Char(string="營業種類")
    businesschexplain = fields.Char(string="中文說明")
    accountp = fields.Char(string="帳簿處理員")#之後要調成many2one
    accountsignp = fields.Char(string="簽証會計師")#之後要調成many2one
    groupclass = fields.Char(string="組織種類")
    accountcost = fields.Integer(string="帳務費用")
    transactdate = fields.Date(string="交易日期")
    declaremathod = fields.Selection(
        [('1','書審'),('2','查帳'),('3','簽證'),('4','所得額標準')],'申報方式')
    undertakep = fields.Char('承辦人員')
    declareclass = fields.Char('申報類別')
    endmediadeclare = fields.Boolean('結算後媒體申報')
    standerdid = fields.Char('標準代號')
    business = fields.Char('經營業務')
    classsite = fields.Char('隸屬業別')
    estimatedoperatingcostrate = fields.Integer('營業成本預估率')
    estimatedoperatingexpensesrate = fields.Integer('營業費用預估率')
    industrystandardcostrate = fields.Integer('同業標準成本率')
    industrystandardexpensesrate = fields.Integer('同業標準費用率')
    #備註說明
    remarktag = fields.Html('備註說明')
    companyread = fields.Char(' ', compute="_onchange_company")

    @api.onchange('company')
    def _onchange_company(self):
        self.companyread = self.company

