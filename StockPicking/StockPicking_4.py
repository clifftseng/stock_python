from haohaninfo import MarketInfo

# 取融資融券資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = MarketInfo.GetMarketInfo('4002','All','20200622','20200623')

for i in Data:
    print(i)
    
