from haohaninfo import GOrder   # 匯入模組

Broker = 'Simulator'  # Yuanta(元大證券)、Capital(群益證券)、Capital_Future(群益期貨)、Kgi(凱基證券)、Kgi_Future(凱基期貨)、Simulator(虛擬期貨)
Kind = 'match'        # match(成交資訊)、commission(委託資訊)、updn5(上下五檔資訊)
Prod = 'TXFJ9'        # 商品代碼(GOrder內需先訂閱該商品)
lastMinute = None     # 存放上一筆資料的分鐘
Close = []            # 存放每分鐘的收盤價
N = 5                 # 定義MA期數

# 串接GOrder即時報價
GO = GOrder.GOQuote()
for i in GO.Describe(Broker,Kind,Prod):
    time = i[0]                 # 時間
    minute = time[14:16]        # 分鐘
    price = float(i[2])         # 價格
    
    if minute == lastMinute:    # 同一分鐘
        Close[-1] = price       # 不斷更新最近一根K棒的收盤價
    else:                       # 不同分鐘
        Close.append(price)     # 新增一根K棒的收盤價

    if len(Close) > N:         # 陣列裡的收盤價數量足夠就可以開始計算MA指標
        thisMA = sum(Close[-N:])/N      # 當前MA值
        lastMA = sum(Close[-N-1:-1])/N  # 上一分鐘MA值
        thisClose = Close[-1]           # 當前收盤價
        lastClose = Close[-2]           # 上一分鐘收盤價
        
        # 黃金交叉(收盤價由下往上穿越MA值)
        if lastClose <= lastMA and thisClose > thisMA:
            print(time,'黃金交叉')
            GO.EndDescribe()
        # 死亡交叉(收盤價由上往下穿越MA值)
        elif lastClose >= lastMA and thisClose < thisMA:
            print(time,'死亡交叉')
            GO.EndDescribe()
            
    lastMinute = minute        # 記錄當前分鐘
    