# coding=utf-8
from openerp import models, fields, api

class setting_aid_systemall(models.TransientModel):
    _name = 'setting.aid.systemall'

    summons = fields.Selection(
        [('monthday','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenuday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='傳票號碼')
    buysell = fields.Selection(
        [('monthday','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='進銷單號')
    consumables = fields.Selection(
        [('monthday','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='耗料單號')
    openaccount = fields.Selection(
        [('monthday','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='立沖單號')
    purchasorder = fields.Selection(
        [('monthday','月日流水號'),('month','月流水號'),('year','流水號'),('free','自行輸入')
         ,('threenumday','前三碼+月日流水號'),('threemonth','前三碼+月流水號')],string='採購單號')
    summonscode = fields.Char('傳票單代號')
    buysellcode = fields.Char('進銷單代號')
    consumablescode = fields.Char('耗料單代號')
    openaccountcode = fields.Char('立沖單代號')
    purchasordercode = fields.Char('採購單代號')
    #其他設定
    numclass = fields.Boolean('單號含單別')
    numyear = fields.Boolean('單號含年度')
    buyseleqsum = fields.Boolean('進銷單號同傳票號碼')
    syncwcpa = fields.Boolean('同步處理WCPA客戶資料')
    beewarn = fields.Boolean('以嗶聲提示警告')
    beecard = fields.Boolean('使用音效卡')  #勾選以嗶聲提示警告時開放勾選，未勾選表示以電腦的蜂鳴器發出嗶聲。
    addfast = fields.Boolean('地址快速輸入')
    negred = fields.Boolean('工程報表負數顯示紅字')
    county = fields.Char('開窗縣市初值')  #開啟地址快速輸入視窗時，會以此設定的縣市名稱先顯示。
    screenfont = fields.Selection([('timesnewbig','新細明體'),('marked','標楷體')],string='螢幕字型')  #選擇螢幕上顯示的字體，細明體（比較大）或標楷體。
    reportfont = fields.Selection([('timesnewbig','新細明體'),('marked','標楷體')],string='報表字型')
    windozoom = fields.Integer('螢幕縮放％')
    #傳真、預覽
        #1.傳真設定
    outsidenum = fields.Char('撥外線前應先撥的數字(0-9或空白)')
    busyreplay = fields.Char('對方忙線預設重撥次數(0-9)')
    busywait = fields.Char('忙線擬在重撥等待秒數(0-99)')
    areanum = fields.Char('目前所在區域號碼(ex.02)')
        #2.一般報表預覽方式
    Multiple = fields.Boolean('同時可選擇多加用戶，批次瀏覽(限登錄用戶才可追帳)')
    single = fields.Boolean('每次只選擇一家用戶，瀏覽時切換，依切換用戶，設為登錄用戶')
    #mail設定。估價驗收之工程請款單可依此設定做為E-mail 之寄件者資料。其中「外寄郵件伺服器(帳號)、密碼」不一定會需要，必須視該 Mail Server是否允許匿名E-mail，如不允許則必須輸入正確的帳號、密碼，才能正確與 Mail Server 連線。
    custom = fields.Boolean('自訂')
    gmail = fields.Boolean('Gmail')
    hotmail = fields.Boolean('Hotmail')
    email = fields.Char('Mail')
    mserversmtp = fields.Char('外寄郵件伺服器(SMTP)')
    port = fields.Char('連接埠')
    mserveracct = fields.Char('外寄郵件伺服器(帳號)')
    code = fields.Char('密碼')

    powonnumlockon = fields.Boolean('系統啟動時，自動啟動NumLock鍵')
    tabopen = fields.Boolean('以頁籤型態，顯示開啟中視窗')  #這裡要看文件裡的說明
    creatdate = fields.Date('建立日')
    editdate = fields.Date('修改日')
    updater = fields.Char('更新者')