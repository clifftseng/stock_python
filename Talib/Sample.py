from Talib_GetData import GetKBar

flag = 0                   
KBar = GetKBar('500','TXF','Future','1')   # 取Talib套件適用的K棒資料

for i in range(0,len(KBar['date'] )):
    Date = KBar['date'][i]      # 當前日期
    NowOpen = KBar['open'][i]   # 當前日K棒的開盤價
    NowHigh = KBar['high'][i]   # 當前日K棒的最高價
    NowLow = KBar['low'][i]     # 當前日K棒的最低價
    NowClose = KBar['close'][i] # 當前日K棒的收盤價
    
    # 當日K棒有經過9950點就進場
    if flag == 0 and NowHigh >= 9950 and NowLow <= 9950:
        flag = 1
        OrderDate = Date
        OrderPrice = 9950
        
    # 進場後價格超過10000點
    elif flag == 1 and NowHigh >= 10000:
        flag = 2
        MaxHigh = NowHigh
        
    # 開始出場判斷
    if flag == 2:
        # 持續更新最高價
        MaxHigh = max( MaxHigh , NowHigh )
        # 超過10000點後的高點減掉9950的30%
        StopLoss = (MaxHigh-9950)*0.3
        # 停損點位
        StopPoint = MaxHigh - StopLoss
        # 開盤就觸價
        if NowOpen <= StopPoint:
            flag = 0
            CoverDate = Date
            CoverPrice = NowOpen
            print('Buy',OrderDate,OrderPrice,'Sell',CoverDate,CoverPrice)
        # 盤中才觸價
        elif NowLow <= StopPoint:
            flag = 0
            CoverDate = Date
            CoverPrice = StopPoint
            print('Buy',OrderDate,OrderPrice,'Sell',CoverDate,CoverPrice)
            