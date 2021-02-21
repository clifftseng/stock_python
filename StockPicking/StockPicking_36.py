import haohaninfo

# 三大法人買賣超資訊 (資訊代碼，股票標的)
Data = haohaninfo.MarketInfo.GetMarketInfo('4004','All','20210115','20211231')
ProdList = sorted(set([ i[1] for i in Data ]))

# 逐檔股票判斷
for Prod in ProdList:
    # 近三日資料
    Data_P = [ i for i in Data if i[1] == Prod ][-3:]
    # 外資從投信或自營商收籌碼的天數
    Num = 0
    for i in Data_P:
        if int(i[5]) > 0 and (int(i[11]) < 0 or int(i[15]) < 0):
           Num += 1 
    # 近三日都符合條件
    if Num >= 3:
        # 取該公司的資本額
        Capital = haohaninfo.MarketInfo.GetMarketInfo('3001', '2409')[0][13]
        Capital = int(Capital.strip('元').split(':')[1])
        # 資本額超過 800億
        if Capital >= 80000000000:
            print(Prod)

