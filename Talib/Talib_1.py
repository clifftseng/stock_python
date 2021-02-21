# 匯入套件
from haohaninfo import GOrder 
from talib.abstract import * 
import numpy as np

Data = GOrder.GetHistoryKBar('100','1101','Stock','1')  # 取歷史報價
Data = [ i.strip('\n').split(',') for i in Data ]       # 刪除換行符號並依逗號分隔

# 將資料改為Talib套件適用的格式
KBar = {}
KBar['date'] = np.array([ i[0] for i in Data ])
KBar['open'] = np.array([ float(i[2]) for i in Data ])
KBar['high'] = np.array([ float(i[3]) for i in Data ])
KBar['low'] = np.array([ float(i[4]) for i in Data ])
KBar['close'] = np.array([ float(i[5]) for i in Data ])
KBar['volume'] = np.array([ int(i[6]) for i in Data ])

N = 5             # 定義MA指標期數，5就代表5日MA
MA = SMA(KBar,N)  # 利用Talib套件計算MA指標

# 印出每日MA值
for i in range(0,len(MA)):
    print( KBar['date'][i] , round(MA[i],2) )
    