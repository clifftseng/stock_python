# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *
import matplotlib.pyplot as plt
import numpy as np

KBar = GetKBar('300','2330','Stock','1')  # 取Talib套件適用的K棒資料
Date = KBar['date']                   # 資料日期 (X軸)
Close = KBar['close']                 # 每日收盤價 (Y軸)
DIF,MACDD,OSC = MACD(KBar,12,26,9)    # 利用Talib套件計算MACD指標 (Y軸)
for i in range(0,33):                 # 將空值預設為 0
    DIF[i],MACDD[i],OSC[i] = 0,0,0

ax1 = plt.subplot(211)                # 新增圖表(列,欄,第1張)
plt.title('Close')                    # 定義圖表名稱
ax1.set_xticks(range(0,len(Date),30)) # 設定時間軸刻度 (開始,結束,間隔)
ax1.set_xticklabels(Date[::30])       # 設定時間軸標籤 (每10日為單位)
ax1.plot(Date,Close,'k-')             # 繪製收盤價折線圖(黑色)

ax2 = plt.subplot(212)                # 新增圖表(列,欄,第2張)
plt.title('OSC')                      # 定義圖表名稱
ax2.set_xticks(range(0,len(Date),30)) # 設定時間軸刻度 (開始,結束,間隔)
ax2.set_xticklabels(Date[::30])       # 設定時間軸標籤 (每10日為單位)
ax2.plot(Date,OSC,'b-')               # 繪製OSC值折線圖(藍色)
ax2.plot(Date,[0]*len(OSC),'k--')     # 繪製虛線(黑色)

plt.show()                            # 顯示圖表


