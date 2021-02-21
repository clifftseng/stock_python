from haohaninfo import MarketInfo

# 公司全體持股資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3005','All')
# 列出所有的股票代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))

# 逐商品判斷
for Prod in ProdList:
    Data1 = [ i for i in Data if i[1] == Prod ]     # 該商品全部資料
    ThisBigStockHolder = int(Data1[-1][4])          # 當月的大股東持有股數
    LastBigStockHolder = int(Data1[-2][4])          # 上個月的大股東持有股數

    if LastBigStockHolder == 0 and ThisBigStockHolder > 0:
        print(Prod,'百分之十以上大股東持有股數 由零轉正') 
    elif LastBigStockHolder > 0 and ThisBigStockHolder == 0:
        print(Prod,'百分之十以上大股東持有股數 由正轉零')
        
    