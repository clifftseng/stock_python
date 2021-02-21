# 匯入模組  
from Talib_GetData import GetKBar
import matplotlib.pyplot as plt
import talib

KBar = GetKBar('301','2330','Stock','1') # 取Talib套件適用的K棒資料
Date = KBar['date']                      # 資料日期 (X軸)
Close = KBar['close']                    # 每日收盤價 (第1張圖的Y軸)
Volume = KBar['volume']                  # 每日成交量 (第2張圖的Y軸)
V5 = talib.MA(Volume,5)                  # 每日成交均量 (第2張圖的Y軸)

ax1 = plt.subplot(211)                   # 新增圖表(列,欄,第1張)
plt.title('Close')                       # 定義圖表名稱
ax1.set_xticks(range(0,len(Date),30))    # 設定時間軸刻度 (開始,結束,間隔)
ax1.set_xticklabels(Date[::30])          # 設定時間軸標籤 (每10日為單位)
ax1.plot(Date,Close,'k-')                # 繪製收盤價折線圖(黑色)

ax2 = plt.subplot(212)                   # 新增圖表(列,欄,第2張)
plt.title('Volume')                      # 定義圖表名稱
ax2.set_xticks(range(0,len(Date),30))    # 設定時間軸刻度 (開始,結束,間隔)
ax2.set_xticklabels(Date[::30])          # 設定時間軸標籤 (每10日為單位)
plt.bar(Date,Volume)                     # 繪製成交量柱狀圖(預設藍色)
ax2.plot(Date,V5,'k-')                   # 繪製成交均量折線圖(黑色)
plt.show()                               # 顯示圖表
