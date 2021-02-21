from haohaninfo import MarketInfo

# 均線期數
Fast_N = 3   # 三個月
Slow_N = 36  # 三年

# 公司全體持股資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3005','All')
# 列出所有的股票代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))

# 逐商品判斷
for Prod in ProdList:
    Data1 = [ i for i in Data if i[1] == Prod ]     # 該商品全部資料
    Data2 = [ int(i[2]) for i in Data1 ]            # 董事及監察人持有股數
    ThisFastMA = sum(Data2[-Fast_N:]) / Fast_N      # 當月的快線
    ThisSlowMA = sum(Data2[-Slow_N:]) / Slow_N      # 當月的慢線
    LastFastMA = sum(Data2[-Fast_N-1:-1]) / Fast_N  # 上個月的快線
    LastSlowMA = sum(Data2[-Slow_N-1:-1]) / Slow_N  # 上個月的慢線

    # 近三個月均線 由下往上穿越 近三年均線
    if LastFastMA <= LastSlowMA and ThisFastMA > ThisSlowMA:
        print(Prod,'董事及監察人持有股數 黃金交叉')
        
    # 近三個月均線 由上往下穿越 近三年均線
    elif LastFastMA >= LastSlowMA and ThisFastMA < ThisSlowMA:
        print(Prod,'董事及監察人持有股數 死亡交叉')
        
    