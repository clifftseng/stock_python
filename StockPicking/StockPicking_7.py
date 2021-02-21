import haohaninfo

# 取三大法人買賣超資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data_4004 = haohaninfo.MarketInfo.GetMarketInfo('4004','All','20200701','20201231')
# 取融資融券資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data_4002 = haohaninfo.MarketInfo.GetMarketInfo('4002','All','20200701','20201231')

# 商品代碼清單
ProdList_4004 = sorted(set([ i[1] for i in Data_4004 ]))
ProdList_4002 = sorted(set([ i[1] for i in Data_4002 ]))
ProdList = list( set(ProdList_4004) & set(ProdList_4002) ) # 取兩者的聯集

# 逐檔股票篩選
for Prod in ProdList:
    # 該商品每日的資料
    Data1_4004 = [ i for i in Data_4004 if i[1] == Prod ]
    Data1_4002 = [ i for i in Data_4002 if i[1] == Prod ]
    # 該商品欲回測日期的前三日資料
    Data2_4004 = Data1_4004[-3:]
    Data2_4002 = Data1_4002[-3:]
    # 三大法人買超
    Data3_4004 = [ i for i in Data2_4004 if float(i[19]) > 0 ]
    # 融資餘額減少 且 融券餘額增加
    Data3_4002 = [ i for i in Data2_4002 if float(i[7])-float(i[6]) < 0 and float(i[13])-float(i[12]) > 0 ]
    # 篩選出連三日 三大法人看多 且 散戶看空 的股票標的
    if len(Data3_4004) == 3 and len(Data3_4002) == 3:
        print(Prod)
    
