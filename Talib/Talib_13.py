# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *

KBar = GetKBar('100','2330','Stock','1')  # 取Talib套件適用的K棒資料
TotalProfit = []      # 用來記錄每筆損益
flag = 0              # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
R = RSI(KBar,6)       # 利用Talib套件計算期數為6日的RSI指標

for i in range(6,len(R)-1):
    nextDate = KBar['date'][i+1]
    nextOpen = KBar['open'][i+1]
    thisR = R[i]
    lastR = R[i-1]
    
    # RSI值由下往上穿越50
    if lastR < 50 and thisR > 50:
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
    # RSI值由上往下穿越50
    elif lastR > 50 and thisR < 50:
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
    # RSI值大於80
    elif flag == 1 and thisR > 80:
        # 多單平倉
        CoverDate = nextDate
        CoverPrice = nextOpen
        Profit = round(CoverPrice - OrderPrice, 2)
        TotalProfit.append(Profit)
        print('B',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
    # RSI值小於20
    elif flag == -1 and thisR < 20:
        # 空單平倉
        CoverDate = nextDate
        CoverPrice = nextOpen
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
    