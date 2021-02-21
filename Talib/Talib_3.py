# 匯入套件
from haohaninfo import GOrder
from Talib_GetData import GetKBar
from talib.abstract import * 

KBar = GetKBar('100','2330','Stock','1')  # 取Talib套件適用的K棒資料
N = 5             # 定義WMA指標期數，5就代表5日WMA
MA = WMA(KBar,N)  # 利用Talib套件計算WMA指標

# 印出每日WMA值
for i in range(0,len(MA)):
    print( KBar['date'][i] , round(MA[i],2) )
    