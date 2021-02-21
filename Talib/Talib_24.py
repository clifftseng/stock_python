# 匯入模組  
from Talib_GetData import GetKBar
import talib

N = 5                      # 當前價格要突破近5日的最高或最低價
StopLoss = 0.05            # 移動式停損百分比
TotalProfit = []           # 用來記錄每筆損益
flag = 0                   # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
KBar = GetKBar('1000','2330','Stock','1')      # 取Talib套件適用的K棒資料
KBar['AvgVolume'] = talib.MA(KBar['volume'],N) # 近N日的成交均量

for i in range(N,len(KBar['date'] )):
    Date = KBar['date'][i]                 # 當前日期
    NowClose = KBar['close'][i]            # 當前日K棒的收盤價
    NowHigh = KBar['high'][i]              # 當前日K棒的最高價
    NowLow = KBar['low'][i]                # 當前日K棒的最低價
    MaxPrice = max(KBar['high'][i-N:i])    # 近N日最高價
    MinPrice = min(KBar['low'][i-N:i])     # 近N日最低價
    NowVolume = KBar['volume'][i]          # 當前日K棒的成交量
    AvgVolume = KBar['AvgVolume'][i]       # 當前日K棒的成交均量
    
    # 多單進場 (空手 且 當日收盤價突破近N日最高價 且 成交量突破近N日均量的1.5倍)
    if flag == 0 and NowClose > MaxPrice and NowVolume > AvgVolume * 1.5:
        flag = 1
        OrderDate = Date
        OrderPrice = NowClose
        AfterOrder_High = NowClose # 進場後最高價
        
    # 多單進場 (空手 且 當日收盤價跌破近N日最低價 且 成交量突破近N日均量的1.5倍)
    elif flag == 0 and NowClose < MinPrice and NowVolume > AvgVolume * 1.5:
        flag = -1
        OrderDate = Date
        OrderPrice = NowClose
        AfterOrder_Low = NowClose # 進場後最低價
    
    # 持有多單
    elif flag == 1:
        # 進場後持續更新最高價
        AfterOrder_High = max( AfterOrder_High , NowHigh )  
        # 當日收盤價符合移動式停損條件 (也可以改用當日開盤價或最低價來判斷)
        if NowClose <= AfterOrder_High * (1-StopLoss):  
            flag = 0
            CoverDate = Date
            CoverPrice = NowClose
            Profit = round(CoverPrice - OrderPrice, 2)
            TotalProfit.append(Profit)
            print('B',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
    
    # 持有空單
    elif flag == -1:
        # 進場後持續更新最低價
        AfterOrder_Low = min( AfterOrder_Low , NowLow )
        # 當日收盤價符合移動式停損條件 (也可以改用當日開盤價或最高價來判斷)
        if NowClose >= AfterOrder_Low * (1+StopLoss):
            flag = 0
            CoverDate = Date
            CoverPrice = NowClose
            Profit = round(OrderPrice - CoverPrice, 2)
            TotalProfit.append(Profit)
            print('S',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
            
# -----------------------------------計算績效-------------------------------------
    
Total = sum(TotalProfit)  # 總損益
Num = len(TotalProfit)    # 總交易次數
Avg = Total / Num         # 平均損益
WinRate = len([ i for i in TotalProfit if i > 0 ]) / Num   # 勝率
print('總損益:',round(Total,2))
print('總交易次數:',Num)
print('平均損益:',round(Avg,2))
print('勝率:',round(WinRate*100,2),'%')

