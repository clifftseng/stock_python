from haohaninfo import MarketInfo

# 取三大法人買賣超資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = MarketInfo.GetMarketInfo('4004','All','20200601','20200603')

for i in Data:
    print(i)
    
