from haohaninfo import MarketInfo
import matplotlib.pyplot as plt
import datetime

# 取國際大盤指數資訊 (資訊代碼，指數代碼，開始日期，結束日期)
Data1 = MarketInfo.GetMarketInfo('1001','0','20200101','20201231')  # NASDAQ 指數
Data2 = MarketInfo.GetMarketInfo('1001','5','20200101','20201231')  # TWSE 指數
# 日期 (X軸)
DateList1 = [ datetime.datetime.strptime(i[1],'%Y/%m/%d') for i in Data1 ]
DateList2 = [ datetime.datetime.strptime(i[1],'%Y/%m/%d') for i in Data2 ]
# 收盤價 (Y軸)
CloseList1 = [ float(i[2]) for i in Data1 ]
CloseList2 = [ float(i[2]) for i in Data2 ]
# 資料開始及結束時間
SDate1 = Data1[0][1]
EDate1 = Data1[-1][1]
SDate2 = Data2[0][1]
EDate2 = Data2[-1][1]
# 繪製圖表
ax1 = plt.subplot(211)                                   # 定義圖框 (圖1)
plt.title(Data1[0][0] + '   ' + SDate1 + ' - ' + EDate1) # 圖表標題 (圖1)
ax1.plot(DateList1,CloseList1,'k-')                      # 收盤價   (圖1)
ax2 = plt.subplot(212)                                   # 定義圖框 (圖2)
plt.title('TWSE' + '   ' + SDate2 + ' - ' + EDate2)      # 圖表標題 (圖2)
ax2.plot(DateList2,CloseList2,'k-')                      # 收盤價   (圖2)
plt.show()                                               # 顯示圖表
