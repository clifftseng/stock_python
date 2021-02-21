from haohaninfo import MarketInfo

# 公司基本資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3001','2330')[0]

for i in Data:
    print(i)
    