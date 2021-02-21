from haohaninfo import MarketInfo

# 取融資融券資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = MarketInfo.GetMarketInfo('4002','All','20200615','20201231')

# 商品代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))

# 逐檔股票篩選
for Prod in ProdList:
    # 該商品每日的資料
    Data1 = [ i for i in Data if i[1] == Prod ]
    # 該商品欲回測日期的前三日資料
    Data2 = Data1[-3:]
    # 融資變動額 & 融券變動額
    Data3 = [ [ float(i[7])-float(i[6]) , float(i[13])-float(i[12]) ,i[0] ] for i in Data2 ]
    # 融資餘額減少 且 融券餘額增加
    Data4 = [ i for i in Data3 if i[0] < 0 and i[1] > 0 ]
    # 篩選出前三日 融資餘額皆減少 且 融券餘額皆增加 的股票標的
    if len(Data4) >= 3:
        print(Prod)
    
