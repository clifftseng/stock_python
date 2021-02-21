# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *

KBar = GetKBar('1000','2330','Stock','1')  # 取Talib套件適用的K棒資料
TotalProfit = []       # 用來記錄每筆損益
flag = 0               # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
FastRSI = RSI(KBar,6)  # 利用Talib套件計算期數為6日的RSI指標
SlowRSI = RSI(KBar,12) # 利用Talib套件計算期數為12日的RSI指標

for i in range(12,len(SlowRSI)-1):
    nextDate = KBar['date'][i+1]
    nextOpen = KBar['open'][i+1]
    thisFastRSI = FastRSI[i]
    thisSlowRSI = SlowRSI[i]
    lastFastRSI = FastRSI[i-1]
    lastSlowRSI = SlowRSI[i-1]
    
    # 多單進場 (短RSI由下往上穿越長RSI)
    if flag == 0 and lastFastRSI < lastSlowRSI and thisFastRSI > thisSlowRSI:
        flag = 1
        OrderDate = nextDate
        OrderPrice = nextOpen   
    # 空單進場 (長RSI由上往下穿越長RSI)
    elif flag == 0 and lastFastRSI > lastSlowRSI and thisFastRSI < thisSlowRSI:
        flag = -1
        OrderDate = nextDate
        OrderPrice = nextOpen

    # 多單出場 (短RSI>80)
    if flag == 1 and thisFastRSI > 80:
        flag = 0
        CoverDate = nextDate
        CoverPrice = nextOpen
        Profit = round(CoverPrice - OrderPrice, 2)
        TotalProfit.append(Profit)
        print('B',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
    # 空單出場 (短RSI<20)
    elif flag == -1 and thisFastRSI < 20:
        flag = 0
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
    