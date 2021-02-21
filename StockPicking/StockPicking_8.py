from haohaninfo import MarketInfo

# 取公司配息資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3006','1586')

for i in Data:
    print(i)
    
