from haohaninfo import MarketInfo

# 取集保股權分散資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = MarketInfo.GetMarketInfo('4001','2330','20201106','20201106')

for i in Data:
    print(i)
    
