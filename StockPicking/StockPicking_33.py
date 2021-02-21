from haohaninfo import MarketInfo

# 公司月營收資訊 (資訊代碼，股票標的)
Data1 = MarketInfo.GetMarketInfo('3003','All')
# 取公司配息資訊 (資訊代碼，股票標的)
Data2 = MarketInfo.GetMarketInfo('3006','All')
# 商品清單
ProdList = sorted(set([ i[1] for i in Data2 ]))

for Prod in ProdList:
    # 該商品資料
    Data3 = [ i for i in Data2 if i[1] == Prod ]
    # 該商品近10年資料
    Data4 = Data3[-10:]
    # 該商品近10年的現金股利
    Data5 = [ i[2] for i in Data4 ]
    # 若資料內有NA值則略過這檔股票
    if 'NA' in Data5:
        continue
    # 將股利資訊從 字串型態 轉為 浮點位型態
    Data6 = [ float(i) for i in Data5 ]
    # 近10年發放現金股利的次數
    Num = len([ i for i in Data6 if float(i) > 0 ])
    # 連續10年都有發放現金股利
    if Num >= 10:
        # 每一年發放的現金股利都不低於前一年
        Check = True
        for i in range(1,10):
            if Data6[i] < Data6[i-1]:
                Check = False
                break
        # 符合條件的股票
        if Check == True:
            Data7 = [ i for i in Data1 if i[1] == Prod ]
            Data8 = float(Data7[-1][-1])
            # 今年到目前為止的累計年營收較去年同期高
            if Data8 > 0:
                print(Prod)

