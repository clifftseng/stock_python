from haohaninfo import MarketInfo
import matplotlib.pyplot as plt
import datetime

# 取集保股權分散資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = MarketInfo.GetMarketInfo('4001','2330','20200701','20201231')
# 取出持股超過 1,000,001 股以上的資訊
Data1 = [ i for i in Data if i[2] == '1000001以上' ]  

# 至少要有三週以上的資料，圖片才不會太難看
if len(Data1) >= 3:
    # 取出想繪製的資料
    Prod = Data1[0][1]                                                    # 商品代碼
    Time = [ datetime.datetime.strptime(i[0],'%Y%m%d') for i in Data1 ]   # 日期
    People = [ int(i[3]) for i in Data1 ]                                 # 級距15的人數
    Percent = [ float(i[5]) for i in Data1 ]                              # 級距15的權重
    # 開始繪圖
    ax1 = plt.subplot(211)                # 定義圖框(上圖)
    ax1.plot(Time,People)                 # 繪製線圖(上圖)
    plt.title(Prod + ' Range15 People')   # 設定標題(上圖)
    ax2 = plt.subplot(212)                # 定義圖框(下圖)
    ax2.plot(Time,Percent)                # 繪製線圖(下圖)
    plt.title(Prod + ' Range15 Percent')  # 設定標題(下圖)
    plt.show()                            # 顯示圖表
else:
    print('該檔股票資訊不足三週')
