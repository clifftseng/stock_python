from haohaninfo import GOrder   # 匯入模組

N = 10            # 設定MA期數
flag = 0          # 手中部位狀態，0代表空手，1代表持有多單，-1代表持有空單
Data = GOrder.GetHistoryKBar('100','2330','Stock','1')  # 取歷史報價
Data = [ i.strip('\n').split(',') for i in Data ]  # 利用列表推導式將資料轉為List格式

lastClose = None  # 昨日收盤價
lastMA = None     # 昨日MA值
for k in range(N,len(Data)-1):
    price = [ float(i[5]) for i in Data[k-N+1:k+1] ]  # 取近N日的收盤價
    nextDate = Data[k+1][0]         # 隔日日期
    nextOpen = float(Data[k+1][2])  # 隔日開盤價
    thisClose = float(Data[k][5])   # 當日收盤價
    thisMA = sum(price)/N           # 當日MA值
    
    # 第一筆資料無法判斷是否交叉
    if lastClose != None:
        # 收盤價由下往上穿越平均線
        if lastClose <= lastMA and thisClose > thisMA:
            # 多單進場
            if flag == 0:
                flag = 1
                OrderDate = nextDate
                OrderPrice = nextOpen
            # 將空單平倉，並多單進場
            elif flag == -1:
                # 先平倉，並記錄損益
                CoverDate = nextDate
                CoverPrice = nextOpen
                Profit = OrderPrice - CoverPrice
                print('S',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
                # 再反向進場
                flag = 1
                OrderDate = nextDate
                OrderPrice = nextOpen
        # 收盤價由上往下穿越平均線
        elif lastClose >= lastMA and thisClose < thisMA:
            # 空單進場
            if flag == 0:
                flag = -1
                OrderDate = nextDate
                OrderPrice = nextOpen
            # 將多單平倉，並空單進場
            elif flag == 1:
                # 先平倉，並記錄損益
                CoverDate = nextDate
                CoverPrice = nextOpen
                Profit = CoverPrice - OrderPrice
                print('B',OrderDate,OrderPrice,CoverDate,CoverPrice,Profit)
                # 再反向進場
                flag = -1
                OrderDate = nextDate
                OrderPrice = nextOpen
    lastClose = thisClose    # 記錄收盤價，方便下一筆資料判斷
    lastMA = thisMA          # 記錄MA值，方便下一筆資料判斷
    
