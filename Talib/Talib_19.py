# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *

KBar = GetKBar('301','2330','Stock','1')  # 取Talib套件適用的K棒資料
TotalProfit = []           # 用來記錄每筆損益
flag = 0                   # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
Real = SAR(KBar,0.02,0.2)  # 利用Talib套件計算SAR指標
FastMA = SMA(KBar,5)       # 利用Talib套件計算MA快線
SlowMA = SMA(KBar,10)      # 利用Talib套件計算MA慢線

for i in range(2,len(Real)-1):
    thisDate = KBar['date'][i]
    thisClose = KBar['close'][i]
    thisSAR = Real[i]
    thisFastMA = FastMA[i]
    thisSlowMA = SlowMA[i]
    
    # 多單出場 (持有多單但SAR指標趨勢轉空)
    if flag == 1 and thisClose < thisSAR:
        flag = 0
        CoverDate = thisDate
        CoverPrice = thisClose
        Profit = round(CoverPrice - OrderPrice, 2)
        TotalProfit.append(Profit)
        print('B',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
    
    # 空單出場 (持有空單但SAR指標趨勢轉多)    
    if flag == -1 and thisClose > thisSAR:
        flag = 0
        CoverDate = thisDate
        CoverPrice = thisClose
        Profit = round(OrderPrice - CoverPrice, 2)
        TotalProfit.append(Profit)
        print('S',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
    
    # 多單進場 (空手 且 SAR指標趨勢偏多 且 MA快線 > MA慢線)
    if flag == 0 and thisClose > thisSAR and thisFastMA > thisSlowMA:
        flag = 1
        OrderDate = thisDate
        OrderPrice = thisClose
    
    # 空單進場 (空手 且 SAR指標趨勢偏空 且 MA快線 < MA慢線)
    if flag == 0 and thisClose < thisSAR and thisFastMA < thisSlowMA:
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
    