from haohaninfo import GOrder   # 匯入模組

N = 10  # 設定MA期數
Data = GOrder.GetHistoryKBar('100','2330','Stock','1')  # 取歷史報價
Data = [ i.strip('\n').split(',') for i in Data ]  # 利用列表推導式將資料轉為List格式

lastClose = None
lastMA = None
for k in range(N,len(Data)):
    date = Data[k-1][0]                           # 日期
    close = float(Data[k-1][5])                   # 收盤價
    price = [ float(i[5]) for i in Data[k-N:k] ]  # 取近N日的收盤價
    MA = sum(price)/N                             # 計算MA值
    
    # 第一筆資料無法判斷是否交叉
    if lastClose != None:
        # 收盤價由下往上穿越平均線
        if lastClose <= lastMA and close > MA:
            print('日期:',date,' 收盤價:',close,' MA值:',MA,' 黃金交叉')
        # 收盤價由上往下穿越平均線
        elif lastClose >= lastMA and close < MA:
            print('日期:',date,' 收盤價:',close,' MA值:',MA,' 死亡交叉')
        # 沒有任何穿越
        else:
            print('日期:',date,' 收盤價:',close,' MA值:',MA)
        
    lastClose = close    # 記錄收盤價，方便下一筆資料判斷
    lastMA = MA          # 記錄MA值，方便下一筆資料判斷
    