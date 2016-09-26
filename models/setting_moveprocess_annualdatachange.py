#-*- coding:utf-8 -*-
from openerp import models, fields, api

class setting_moveprocess_annualdatachange(models.Model):
    _name = 'setting.moveprocess.annualdatachange'

    #年結方式
    compyearcover = fields.Boolean('1-比對年結(覆蓋 新年度和舊年度相同的資料) 票據及銀行資料一律不覆蓋')
    compyearuncover = fields.Boolean('2-比對年結(不覆蓋新年度和舊年度相同的資料) 年度只有一筆資料(ex.設定檔)及開帳金額，皆以舊年度資量覆蓋，請確認')
    newyear = fields.Boolean('3-全新年結(不保留新年度資料)')

    dclrto0bsmrg = fields.Boolean('各類扣繳申報金額為0，基本檔資料一併結轉')
    endstockto0 = fields.Boolean('期末庫存數量與金額為0，不結轉')
    chekticktrenew = fields.Boolean('結帳傳票重新產生')
    findatacarry = fields.Boolean('已完工之工程資料，一併結轉')
    caryBfinenginum = fields.Boolean('只轉B年完工之工程資料')  #適用於重複執行年結（即年結方式=1、2比對年結）且勾選“已完工之工程資料，一併結轉”選項。勾選時，只重新從舊年度轉入新年度已有的工程資料。
    delAfinenginum = fields.Boolean('清除已於A年完工之工程資料')
    cmltgandl = fields.Boolean('累積盈虧之開帳金額不分工程')

    #檔案類別
    pubsetfile = fields.Boolean('公用設定檔')
    pubdatafile = fields.Boolean('公用資料檔')
    ldgrdatafile = fields.Boolean('總帳資料檔')
    proptdatafile = fields.Boolean('財產資料檔')
    engcostdatafile = fields.Boolean('工程成本資料檔')
    paydatafile = fields.Boolean('各類扣繳資料檔')
    towtaxtonedtfile = fields.Boolean('兩稅合一資料檔')
    stlmdclrdtfile = fields.Boolean('結算申報資料檔')
    banktickdtfile = fields.Boolean('銀行票據資料檔')
    estiexamfile = fields.Boolean('估價驗收檔')

    #結轉檔案
    #這裡欄位會因為檔案類別的選擇而變動，所以沒有做
