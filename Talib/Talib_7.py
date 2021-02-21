# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *
import matplotlib.pyplot as plt

KBar = GetKBar('100','2330','Stock','1')  # 取Talib套件適用的K棒資料
Date = KBar['date']   # 資料日期 (X軸)
Close = KBar['close'] # 收盤價 (Y軸)
SMA = SMA(KBar,10)    # 利用Talib套件計算10日SMA指標 (Y軸)
WMA = WMA(KBar,10)    # 利用Talib套件計算10日WMA指標 (Y軸)
EMA = EMA(KBar,10)    # 利用Talib套件計算10日EMA指標 (Y軸)

ax = plt.subplot(111)                # 新增圖表(列,欄,第幾張)
plt.title('Close(Black) SMA(Blue) WMA(Red) EMA(Green)') # 定義圖表名稱
ax.set_xticks(range(0,len(Date),10)) # 設定時間軸刻度 (開始,結束,間隔)
ax.set_xticklabels(Date[::10])       # 設定時間軸標籤 (每10日為單位)
ax.plot(Date,Close,'k-')             # 繪製收盤價折線圖(黑色)
ax.plot(Date,SMA,'b-')               # 繪製SMA折線圖(藍色)
ax.plot(Date,WMA,'r-')               # 繪製WMA折線圖(紅色)
ax.plot(Date,EMA,'g-')               # 繪製EMA折線圖(綠色)
plt.show()                           # 顯示圖表


