from haohaninfo import MarketInfo

# 公司月營收資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3003','All')
# 所有的股票代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))
# 逐檔股票判斷
for Prod in ProdList:
    # 該檔股票的資訊
    Data1 = [ i for i in Data if i[1] == Prod ]
    # 最近6個月的資訊
    Data2 = Data1[-6:]
    # 最近6個月 月營收增加的次數
    Number = len([ i for i in Data2 if int(i[4]) > 0 ])
    # 最近6個月 月營收都增加
    if Number == 6:
        print('股票代號:',Prod,'連續6個月月營收增加')
