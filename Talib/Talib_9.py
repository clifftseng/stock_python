# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *

KBar = GetKBar('100','2317','Stock','1')  # 取Talib套件適用的K棒資料
TotalProfit = []      # 用來記錄每筆損益
flag = 0              # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
K,D = STOCH(KBar,9)   # 利用Talib套件計算期數為9日的KD指標
for i in range(0,12): # 將K及D的空值預設為50
    K[i],D[i] = 50,50 

for i in range(13,len(K)-1):
    nextDate = KBar['date'][i+1]
    nextOpen = KBar['open'][i+1]
    thisK = K[i]
    thisD = D[i]
    lastK = K[i-1]
    lastD = D[i-1]
    
    # K值由下往上穿越D值
    if lastK < lastD and thisK > thisD:
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
    # K值由上往下穿越D值
    elif lastK > lastD and thisK < thisD:
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
    