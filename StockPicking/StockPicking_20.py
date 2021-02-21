from haohaninfo import MarketInfo

# 公司月營收資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3003','2330')

for i in Data:
    print(i)
