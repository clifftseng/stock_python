from haohaninfo import MarketInfo

# 取三大法人買賣超資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = MarketInfo.GetMarketInfo('4004','All','20200601','20211231')

# 商品代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))

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
        print(Prod)
    