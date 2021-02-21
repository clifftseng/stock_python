from haohaninfo import MarketInfo

# 公司董監事持股資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3004','2330')

for i in Data:
    print(i)
    
