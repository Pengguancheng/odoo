#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_aid_accountperson(models.Model):
    _name = 'setting.aid.accountperson'

    pcode = fields.Char('代號')
    mediacode = fields.Char('媒體代號')
    pname = fields.Char('姓名')
    pid = fields.Char('身份證字號')
    pidtag = fields.Selection([('0','正常'),('1','戶政機關給號錯誤'),
                              ('2','外僑')],'證號註記')
    pkind = fields.Selection([('0','律師'),('1','會計師'),('2','稅務代理人'),
                              ('3','公司職員'),('4','記帳士')],'性質')
    #證號代號
    proofcodeyear = fields.Char('年', help="123")
    proofcodeword = fields.Char('字')
    proofcodenum = fields.Char('號')
    proofcode = fields.Char('證書字號',compute="_proofcode", readonly=True )
    area = fields.Char('區局')
    fsc = fields.Selection([('0','N'),('1','Y')],'由金管會簽證')
    officename = fields.Char('事務所名稱')
    standerdid = fields.Char('統一編號')
    withhold = fields.Selection([('0','N'),('1','Y')],'辦理扣繳')
    address = fields.Char('地址')
    zipcode = fields.Char('郵遞區號')
    telephone = fields.Char('電話')
    fox = fields.Char('傳真')
    email = fields.Char('電子郵件')
    logincodeword = fields.Char('字')
    logincodenum = fields.Char('號')
    persontele = fields.Char('電話-聯絡人')
    personteleclass = fields.Char('分機')
    pguildname = fields.Char('加入記帳士公會名稱（縣市名稱）')
    pguildid = fields.Char('加入記帳士公會其會員稱號')

    @api.onchange('proofcodeyear','proofcodeword','proofcodenum')
    def _proofcode(self):
        self.proofcode = "(" + str(self.proofcodeyear) + ")壹財稅(" + str(self.proofcodeword) + ")字第(" + str(self.proofcodenum) + ")號"
