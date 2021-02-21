from haohaninfo import GOrder   # 匯入模組

N = 10  # 設定MA期數
Data = GOrder.GetHistoryKBar('100','2330','Stock','1')  # 取歷史報價
Data = [ i.strip('\n').split(',') for i in Data ]  # 利用列表推導式將資料轉為List格式

for k in range(N,len(Data)):
    date = Data[k-1][0]                           # 日期
    close = Data[k-1][5]                          # 收盤價
    price = [ float(i[5]) for i in Data[k-N:k] ]  # 取近N日的收盤價
    MA = sum(price)/N                             # 計算MA值
    print('日期:',date,' 收盤價:',close,' MA值:',MA)
