from haohaninfo import MarketInfo

# 公司基本資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3001','All')

# 逐檔股票判斷
for i in Data:
    Number = i[0]  # 股票代碼
    Name = i[2]    # 公司名稱
    Date = i[11]   # 公司成立日期
    
    Year = Date.split(':')[1].split('/')[0]  # 先依照冒號分割，再依照斜線分割，最後取出公司成立的民國年
    Year = int(Year)  # 將年份轉為整數型態
    
    # 民國105年後成立的公司
    if Year >= 105:
        print(Date,Number,Name)