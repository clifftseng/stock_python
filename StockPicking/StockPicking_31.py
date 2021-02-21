from haohaninfo import MarketInfo

# 取國際大盤指數資訊 (資訊代碼，指數代碼，開始日期，結束日期)
Data = MarketInfo.GetMarketInfo('1001','0','20200101','20201231')

for i in Data:
    print(i)
    
