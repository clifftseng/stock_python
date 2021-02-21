from haohaninfo import MarketInfo

# 取集保股權分散資訊 (資訊代碼，股票標的，起始日期，結束日期)
Data = MarketInfo.GetMarketInfo('4001','All','20201030','20201119')
# 所有的股票代碼清單
ProdList = sorted(set([ i[1] for i in Data ]))
# 逐檔股票判斷
for Prod in ProdList:
    Data1 = [ i for i in Data if i[1] == Prod ]            # 取出該檔股票的資訊
    Data2 = [ i for i in Data1 if i[2] == '1000001以上' ]  # 取出持股超過 1,000,001 股以上的資訊
    # 至少有兩週以上的資料才判斷，避免程式出現錯誤
    if len(Data2) >= 2:
        ThisWeekPeople = int(Data2[-1][3])     # 這一週 持股超過 1,000,001 股以上 的人數
        LastWeekPeople = int(Data2[-2][3])     # 上一週 持股超過 1,000,001 股以上 的人數
        ThisWeekPercent = float(Data2[-1][5])  # 這一週 持股超過 1,000,001 股以上 的持股權重
        LastWeekPercent = float(Data2[-2][5])  # 上一週 持股超過 1,000,001 股以上 的持股權重
        # 人數增加 且 持股權重增加 3% 以上
        if ThisWeekPeople > LastWeekPeople and ThisWeekPercent > LastWeekPercent + 3:
            print('股票代碼:',Prod,'級距15','這週人數:',ThisWeekPeople,'人','上週人數:',LastWeekPeople,'人','這週權重:',ThisWeekPercent,'%','上週權重:',LastWeekPercent,'%')
        
