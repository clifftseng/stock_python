# 匯入模組  
from Talib_GetData import GetKBar
import matplotlib.pyplot as plt
import numpy as np
import talib

N = 5                      # 當前價格要突破近5日的最高或最低價
TakeProfit = 0.03          # 固定式停利百分比
StopLoss = 0.02            # 固定式停損百分比
flag = 0                   # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
KBar = GetKBar('1000','2330','Stock','1')       # 取Talib套件適用的K棒資料
KBar['AvgVolume'] = talib.MA(KBar['volume'],N) # 近N日的成交均量

MaxAvgProfit = -999   # 最佳的平均損益 (一開始先預設負極值)
# 爆量的倍數
for k in np.arange(1 ,2.1,0.1):
    k = round(k,1)        # 避免python小數點精度問題
    TotalProfit = []      # 用來記錄每筆損益
        
    for i in range(N,len(KBar['date'] )):
        Date = KBar['date'][i]                 # 當前日期
        NowPrice = KBar['close'][i]            # 當前價格
        MaxPrice = max(KBar['close'][i-N:i])   # 近N日最高價
        MinPrice = min(KBar['close'][i-N:i])   # 近N日最低價
        NowVolume = KBar['volume'][i]          # 當前成交量
        AvgVolume = KBar['AvgVolume'][i]       # 當前成交均量
        MaxVolume = max(KBar['volume'][i-N:i]) # 前N日的最大成交量
        
        # 多單進場 (空手 且 當前價格突破近N日最高價 且 成交量突破近N日均量的k倍)
        if flag == 0 and NowPrice > MaxPrice and NowVolume > AvgVolume * k:
            flag = 1
            OrderDate = Date
            OrderPrice = NowPrice
        # 多單進場 (空手 且 當前價格跌破近N日最低價 且 成交量突破近N日均量的k倍)
        elif flag == 0 and NowPrice < MinPrice and NowVolume > AvgVolume * k:
            flag = -1
            OrderDate = Date
            OrderPrice = NowPrice
        
        # 持有多單
        if flag == 1:
            # 停利
            if NowPrice >= OrderPrice * (1+TakeProfit):
                flag = 0
                CoverDate = Date
                CoverPrice = NowPrice
                Profit = round(CoverPrice - OrderPrice, 2)
                TotalProfit.append(Profit)
            # 停損
            elif NowPrice <= OrderPrice * (1-StopLoss):
                flag = 0
                CoverDate = Date
                CoverPrice = NowPrice
                Profit = round(CoverPrice - OrderPrice, 2)
                TotalProfit.append(Profit)
            # 量價背離 (價格突破 但 成交量沒創新高)
            elif NowPrice > MaxPrice and NowVolume <= MaxVolume:
                flag = 0
                CoverDate = Date
                CoverPrice = NowPrice
                Profit = round(CoverPrice - OrderPrice, 2)
                TotalProfit.append(Profit)
        # 持有空單
        elif flag == -1:
            # 停利
            if NowPrice <= OrderPrice * (1-TakeProfit):
                flag = 0
                CoverDate = Date
                CoverPrice = NowPrice
                Profit = round(OrderPrice - CoverPrice, 2)
                TotalProfit.append(Profit)
            # 停損
            elif NowPrice >= OrderPrice * (1+StopLoss):
                flag = 0
                CoverDate = Date
                CoverPrice = NowPrice
                Profit = round(OrderPrice - CoverPrice, 2)
                TotalProfit.append(Profit)
            # 量價背離 (價格跌破 但 成交量沒創新高)
            elif NowPrice < MinPrice and NowVolume <= MaxVolume:
                flag = 0
                CoverDate = Date
                CoverPrice = NowPrice
                Profit = round(OrderPrice - CoverPrice, 2)
                TotalProfit.append(Profit)
    
    try:
        Total = sum(TotalProfit)  # 總損益
        Num = len(TotalProfit)    # 總交易次數
        Avg = Total / Num         # 平均損益
    except:
        continue
    
    # 較佳的平均損益
    if Avg > MaxAvgProfit:
        temp = TotalProfit
        Best_k = k
        MaxAvgProfit = Avg
        
# -----------------------------------計算績效-------------------------------------
    
TotalProfit = temp
Total = sum(TotalProfit)  # 總損益
Num = len(TotalProfit)    # 總交易次數
Avg = Total / Num         # 平均損益
WinRate = len([ i for i in TotalProfit if i > 0 ]) / Num   # 勝率
print('最佳的爆量倍數:',Best_k)
print('總損益:',round(Total,2))
print('總交易次數:',Num)
print('平均損益:',round(Avg,2))
print('勝率:',round(WinRate*100,2),'%')

