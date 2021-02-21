from haohaninfo import MarketInfo

# 取銀行匯率資訊 (資訊代碼，貨幣代碼，開始日期，結束日期)
Data = MarketInfo.GetMarketInfo('1002','13','20200101','20201231')

for i in Data:
    print(i)
    
