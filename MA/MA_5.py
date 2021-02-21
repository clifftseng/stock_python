import matplotlib.pyplot as plt    # 匯入模組

N = 5                  # 定義MA期數
lastM = None           # 存放上一筆資料的分鐘
Time_List = []         # 存放每分鐘的時間
Close_List = []        # 存放每分鐘的收盤價
MA_List = [None]*(N-1) # 存放每分鐘的MA值

# 取資料
data = open('TXFJ9_Match.txt').readlines()         # 開啟同路徑下的資料
data = [ i.strip('\n').split(',') for i in data ]  # 刪除換行符號並依逗號分割成 List

# 計算每分鐘收盤價及MA值
for i in data:
    time = i[0]                 # 時間
    minute = time[14:16]        # 分鐘
    price = float(i[2])         # 價格

    if minute == lastM:              # 同一分鐘
        Time_List[-1] = time[11:16]  # 不斷更新最近一根K棒的時間
        Close_List[-1] = price       # 不斷更新最近一根K棒的收盤價
    else:                            # 不同分鐘
        Time_List.append(time[11:16])# 新增一根K棒的時間
        Close_List.append(price)     # 新增一根K棒的收盤價
        
    if len(Close_List) >= N:         # 陣列裡的收盤價數量足夠就可以開始計算MA指標
        MA = sum(Close_List[-N:])/N  # 期數為N期的MA指標

        if minute == lastM:          # 同一分鐘
            MA_List[-1] = MA         # 不斷更新最近一根K棒的MA值
        else:                        # 不同分鐘
            MA_List.append(MA)       # 新增一根K棒的MA值

    lastM = minute           # 記錄當前分鐘
    

ax = plt.subplot(111)                      # 新增圖表(列,欄,第幾張)
plt.title('Close & MA')                    # 定義圖表名稱
ax.set_xticks(range(0,len(Time_List),20))  # 設定時間軸刻度 (開始,結束,間隔)
ax.set_xticklabels(Time_List[::20])        # 設定時間軸標籤 (每20分鐘為單位)
ax.plot(Close_List,'k-')                   # 繪製價格折線圖(黑色)
ax.plot(MA_List,'b-')                      # 繪製MA值折線圖(藍色)
plt.show()                                 # 顯示圖表


