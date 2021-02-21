# 匯入模組
from haohaninfo import GOrder   
from Talib_GetData import GetKBar
from talib.abstract import *

KBar = GetKBar('100','2330','Stock','1')  # 取Talib套件適用的K棒資料
MA = SMA(KBar,10) # 利用Talib套件計算10日MA指標
TotalProfit = []  # 用來記錄每筆損益
flag = 0          # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單

for i in range(10,len(MA)-1):
    nextDate = KBar['date'][i+1]
    nextOpen = KBar['open'][i+1]
    thisClose = KBar['close'][i]
    lastClose = KBar['close'][i-1]
    thisMA = MA[i]
    lastMA = MA[i-1]
    
    # 收盤價由下往上穿越平均線
    if lastClose <= lastMA and thisClose > thisMA:
        # 多單進場
        if flag == 0:
            flag = 1
            OrderDate = nextDate
            OrderPrice = nextOpen
        # 將空單平倉，並多單進場
        elif flag == -1:
            # 先平倉，並記錄損益
            CoverDate = nextDate
            CoverPrice = nextOpen
            Profit = round(OrderPrice - CoverPrice, 2)
            TotalProfit.append(Profit)
            print('S',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
            # 再反向進場
            flag = 1
            OrderDate = nextDate
            OrderPrice = nextOpen
    # 收盤價由上往下穿越平均線
    elif lastClose >= lastMA and thisClose < thisMA:
        # 空單進場
        if flag == 0:
            flag = -1
            OrderDate = nextDate
            OrderPrice = nextOpen
        # 將多單平倉，並空單進場
        elif flag == 1:
            # 先平倉，並記錄損益
            CoverDate = nextDate
            CoverPrice = nextOpen
            Profit = round(CoverPrice - OrderPrice, 2)
            TotalProfit.append(Profit)
            print('B',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
            # 再反向進場
            flag = -1
            OrderDate = nextDate
            OrderPrice = nextOpen
    
# -----------------------------------計算績效-------------------------------------  

Total = sum(TotalProfit)  # 總損益
Num = len(TotalProfit)    # 總交易次數
Avg = Total / Num         # 平均損益
WinRate = len([ i for i in TotalProfit if i > 0 ]) / Num   # 勝率
print('總損益:',round(Total,2))
print('總交易次數:',Num)
print('平均損益:',round(Avg,2))
print('勝率:',round(WinRate*100,2),'%')
