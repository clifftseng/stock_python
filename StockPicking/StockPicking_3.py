import haohaninfo

# 取三大法人買賣超資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = haohaninfo.MarketInfo.GetMarketInfo('4004','All','20200601','20211231')

# 商品代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))

temp = []
# 逐檔股票篩選
for Prod in ProdList:
    # 該商品每日的資料
    Data1 = [ i for i in Data if i[1] == Prod ]
    # 該商品欲回測日期的前三日資料
    Data2 = Data1[-3:]
    # 欄位為正值代表買超，欄位分別為 外資、投信、自營商
    Data3 = [ i for i in Data2 if float(i[5]) > 0 and float(i[11]) > 0 and float(i[15]) > 0 ]
    # 篩選出前三日三大法人皆買超的股票標的
    if len(Data3) >= 3:
        Data4 = haohaninfo.GOrder.GetHistoryKBar('10',Prod,'Stock','1') # 取近10日K棒
        Data5 = [ i.split(',') for i in Data4 ]     # 依照逗號切割資料
        CloseList = [ float(i[5]) for i in Data5 ]  # 將這10日的收盤價取出
        MA = sum(CloseList) / len(CloseList)        # 計算均線(MA值)
        TodayClose = CloseList[-1]                  # 最近一日的收盤價
        if TodayClose > MA:                         # 最近一日的收盤價在10日MA之上
            print(Prod)
        
        
        