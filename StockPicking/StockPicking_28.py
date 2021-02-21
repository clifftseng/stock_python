from haohaninfo import MarketInfo

# 取信用評等資訊 (資訊代碼，股票代碼)
Data = MarketInfo.GetMarketInfo('2001','2330')

for i in Data:
    print(i)
    
