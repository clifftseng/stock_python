from haohaninfo import MarketInfo

# 公司月營收資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3003','All')
# 所有的股票代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))
# 逐檔股票判斷
for Prod in ProdList:
    # 該檔股票的資訊
    Data1 = [ i for i in Data if i[1] == Prod ]
    # 最近1個月的公司月營收資訊
    Data2 = Data1[-1]
    # 去年同期累計營收
    LastProfit = float(Data2[7])
    # 年營收增減百分比
    ChangeProfit = float(Data2[9])
    
    # 去年同期的月營收大於一億元 且 年營收增減百分比超過100%
    if LastProfit >= 100000 and ChangeProfit >= 100:
        print('股票代號:',Prod,'年營收增減百分比為',ChangeProfit,'%')
    