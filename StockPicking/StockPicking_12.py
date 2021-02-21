from haohaninfo import MarketInfo

# 公司董監事持股資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3004','All')
# 列出所有的股票代碼清單
ProdList = sorted(set([ i[0] for i in Data ]))

for Prod in ProdList:
    Data1 = [ i for i in Data if i[0] == Prod ]  # 該商品資料
    Number = sum([ float(i[4]) for i in Data1 ]) # 內部人總持股數量
    Pledge = sum([ float(i[5]) for i in Data1 ]) # 內部人總設質數量
    try:
        Ratio = Pledge / Number                  # 內部人總設質比例
    except:
        Ratio = 0

    # 篩選出 內部人總設質比例 >= 90% 的股票標的
    if Ratio >= 0.9:
        print('股票代碼:',Prod,'公司內部人總設質比例:',round(Ratio*100,2),'%')
