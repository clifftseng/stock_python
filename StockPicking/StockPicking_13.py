from haohaninfo import MarketInfo

# 公司全體持股資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3005','3008')

for i in Data:
    print(i)
    
