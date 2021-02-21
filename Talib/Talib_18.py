# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *

KBar = GetKBar('301','2330','Stock','1')  # 取Talib套件適用的K棒資料
TotalProfit = []      # 用來記錄每筆損益
flag = 0              # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
Real = SAR(KBar,0.02,0.2)                 # 利用Talib套件計算SAR指標

for i in range(2,len(Real)-1):
    thisDate = KBar['date'][i]
    thisClose = KBar['close'][i]
    lastClose = KBar['close'][i-1]
    thisSAR = Real[i]
    lastSAR = Real[i-1]
    
    # 收盤價由下往上穿越SAR值 (SAR由綠轉紅)
    if lastClose < lastSAR and thisClose > thisSAR:
        # 多單進場
        if flag == 0:
            flag = 1
            OrderDate = thisDate
            OrderPrice = thisClose
        # 將空單平倉，並多單進場
        elif flag == -1:
            # 先平倉，並記錄損益
            CoverDate = thisDate
            CoverPrice = thisClose
            Profit = round(OrderPrice - CoverPrice, 2)
            TotalProfit.append(Profit)
            print('S',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
            # 再反向進場
            flag = 1
            OrderDate = thisDate
            OrderPrice = thisClose
    # 收盤價由上往下穿越SAR值 (SAR由紅轉綠)
    elif lastClose > lastSAR and thisClose < thisSAR:
        # 空單進場
        if flag == 0:
            flag = -1
            OrderDate = thisDate
            OrderPrice = thisClose
        # 將多單平倉，並空單進場
        elif flag == 1:
            # 先平倉，並記錄損益
            CoverDate = thisDate
            CoverPrice = thisClose
            Profit = round(CoverPrice - OrderPrice, 2)
            TotalProfit.append(Profit)
            print('B',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
            # 再反向進場
            flag = -1
            OrderDate = thisDate
            OrderPrice = thisClose
    
# -----------------------------------計算績效-------------------------------------
    
Total = sum(TotalProfit)  # 總損益
Num = len(TotalProfit)    # 總交易次數
Avg = Total / Num         # 平均損益
WinRate = len([ i for i in TotalProfit if i > 0 ]) / Num   # 勝率
print('總損益:',round(Total,2))
print('總交易次數:',Num)
print('平均損益:',round(Avg,2))
print('勝率:',round(WinRate*100,2),'%')
    