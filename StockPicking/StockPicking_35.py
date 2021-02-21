import haohaninfo

# 公司全體持股資訊 (資訊代碼，股票標的)
Data = haohaninfo.MarketInfo.GetMarketInfo('3005','All')
ProdList = sorted(set([ i[1] for i in Data ]))

# 逐檔股票判斷
for Prod in ProdList:
    Data_P = [ i for i in Data if i[1] == Prod ]
    # 跳過資料不足四個月的股票
    if len(Data_P) < 4:
        continue
    # 最近三個月基金經理人皆增加持股
    if int(Data_P[-1][3]) > int(Data_P[-2][3]) > int(Data_P[-3][3]) > int(Data_P[-4][3]):
        KBar = haohaninfo.GOrder.GetHistoryKBar('60',Prod,'Stock','1') # 取近60個交易日的日K棒
        KBar = [ i.split(',') for i in KBar ]                          # 依照逗號切割資料
        if KBar == [['']]:
            continue
        Initial_Price = float(KBar[0][2])                    # 初始股價
        Highest_Price = max([ float(i[3]) for i in KBar ])   # 近60日最高價
        Lowest_Price = min([ float(i[4]) for i in KBar ])    # 近60日最低價
        # 股價在近三個月內波動不超過正負10%
        if Initial_Price*1.1 >= Highest_Price and Initial_Price*0.9 <= Lowest_Price:
            print(Prod)
            