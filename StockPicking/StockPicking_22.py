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
    # 去年同期營收
    LastProfit = float(Data2[3])
    # 最近1個月的 YoY
    Current_YoY = float(Data2[5])
    # 去年同期的月營收大於一億元
    if LastProfit >= 100000 and Current_YoY >= 100:
        print('股票代號:',Prod,'最近1個月的 YoY 為',Current_YoY,'%')
    