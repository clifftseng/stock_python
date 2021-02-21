from haohaninfo import MarketInfo

# 取公司配息資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3006','All')
ProdList = sorted(set([ i[1] for i in Data ]))

for Prod in ProdList:
    # 該商品資料
    Data1 = [ i for i in Data if i[1] == Prod ]
    # 該商品近10年資料
    Data2 = Data1[-10:]
    # 該商品近10年的現金股利
    Data3 = [ i[2] for i in Data2 ]
    # 若資料內有NA值則略過這檔股票
    if 'NA' in Data3:
        continue
    # 將股利資訊從 字串型態 轉為 浮點位型態
    Data4 = [ float(i) for i in Data3 ]
    # 近10年發放現金股利的次數
    Num = len([ i for i in Data4 if float(i) > 0 ])
    # 連續10年都有發放現金股利
    if Num >= 10:
        # 每一年發放的現金股利都不低於前一年
        Check = True
        for i in range(1,10):
            if Data3[i] < Data3[i-1]:
                Check = False
                break
        # 印出符合條件的股票代碼及近10年發放的現金股利
        if Check == True:
            print(Prod,Data4)
        