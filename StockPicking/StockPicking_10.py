from haohaninfo import MarketInfo
from haohaninfo import GOrder

# 取公司配息資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3006','All')
ProdList = sorted(set([ i[1] for i in Data ]))

for Prod in ProdList:
    # 該商品資料
    Data1 = [ i for i in Data if i[1] == Prod ]
    # 該商品近10年資料
    Data2 = Data1[-10:]
    # 該商品近10年的現金股利
    Data3 = [ i[2] for i in Data2 ]
    # 若資料內有NA值則略過這檔股票
    if 'NA' in Data3:
        continue
    # 將股利資訊從 字串型態 轉為 浮點位型態
    Data4 = [ float(i) for i in Data3 ]
    # 近10年發放現金股利的次數
    Num = len([ i for i in Data4 if float(i) > 0 ])
    # 連續10年都有發放現金股利
    if Num >= 10:
        # 每一年發放的現金股利都不低於前一年
        Check = True
        for i in range(1,10):
            if Data3[i] < Data3[i-1]:
                Check = False
                break
        # 印出符合條件的股票代碼及近10年發放的現金股利
        if Check == True:
            # 取該檔股票的歷史日K棒 (K棒數量,商品代碼,商品種類,日夜盤)
            KBar = GOrder.GetHistoryKBar('250', Prod, 'Stock', '1')
            # 目前無法取到上櫃股票的歷史資料
            if KBar != ['']:
                Close = [ i.split(',') for i in KBar ] # 依照逗號分隔欄位
                Close = [ float(i[5]) for i in Close ] # 取出收盤價
                MA250 = round(sum(Close)/250,2)        # 計算年均線(一年約250個交易日)
                TodayClose = Close[-1]                 # 最近一日的收盤價
                # 收盤價 > 年均線
                if TodayClose > MA250:
                    print(Prod,'TodayClose:',TodayClose,'MA250:',MA250)
            