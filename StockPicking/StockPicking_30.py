from haohaninfo import MarketInfo
import matplotlib.pyplot as plt
import datetime

# 均線的期數 (60日約為季線)
N = 60
# 取銀行匯率資訊 (資訊代碼，貨幣代碼，開始日期，結束日期)
Data = MarketInfo.GetMarketInfo('1002','13','20200101','20201231')
# 日期 (X軸)
DateList = [ datetime.datetime.strptime(i[1],'%Y/%m/%d') for i in Data ]
# 收盤價 (Y軸 黑色實線)
CloseList = [ float(i[5]) for i in Data ]
# 平均價 (Y軸 藍色虛線)
MA = [None]*(N-1)
for i in range(N,len(CloseList)+1):
    MA.append( sum(CloseList[i-N:i]) / N )
# 貨幣代碼
Prod = Data[0][0].split('(')[1].strip(')')
# 資料開始及結束時間
SDate = Data[0][1]
EDate = Data[-1][1]
# 繪製圖表
ax = plt.subplot(111)                             # 定義圖框
plt.title(Prod + '   ' + SDate + ' - ' + EDate)   # 圖表標題
plt.plot(DateList,CloseList,'k-')                 # 收盤價 (黑色實線)
plt.plot(DateList,MA,'b--')                       # 平均價 (藍色虛線)
plt.show()                                        # 顯示圖表
