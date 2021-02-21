# 匯入模組  
from Talib_GetData import GetKBar
from talib.abstract import *
import matplotlib.pyplot as plt

KBar = GetKBar('301','2330','Stock','1')  # 取Talib套件適用的K棒資料
Date = KBar['date']                       # 資料日期 (X軸)
Close = KBar['close']                     # 每日收盤價 (Y軸)
Real = SAR(KBar,0.02,0.2)                 # 利用Talib套件計算SAR指標 (Y軸)

# 將SAR指標分為紅點與綠點
Real_Red = [None]
Real_Green = [None]
for i in range(1,len(Real)):
    R = Real[i] 
    C = KBar['close'][i]
    # 收盤價 > SAR值，視為紅點
    if C > R:
        Real_Red.append(R)
        Real_Green.append(None)
    # 收盤價 < SAR值，視為綠點
    elif C < R:
        Real_Red.append(None)
        Real_Green.append(R)

ax1 = plt.subplot(111)                            # 新增圖表(列,欄,第1張)
plt.title('Close & SAR')                          # 定義圖表名稱
ax1.set_xticks(range(0,len(Date),30))             # 設定時間軸刻度 (開始,結束,間隔)
ax1.set_xticklabels(Date[::30])                   # 設定時間軸標籤 (每10日為單位)
ax1.plot(Date,Close,'k-')                         # 繪製收盤價折線圖(黑色)
# 參數說明 (X軸,Y軸,圖型大小,圖型顏色,圖案形狀)
plt.scatter(Date,Real_Red,s=1,c='r',marker='o')   # 繪製紅點
plt.scatter(Date,Real_Green,s=1,c='g',marker='o') # 繪製綠點

plt.show()                                        # 顯示圖表


