from haohaninfo import MarketInfo

# 公司基本資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3001','All')

# 逐檔股票判斷
for i in Data:
    Number = i[0]    # 股票代碼
    Name = i[2]      # 公司名稱
    Capital = i[13]  # 實收資本額
    
    Cap = Capital.split(':')[1].replace('元','')  # 先依照冒號分割，再將 '元' 的字串刪除
    Cap = int(Cap)  # 將實收資本額轉為整數型態
    
    # 實收資本額超過一仟億的公司
    if Cap >= 100000000000:
        print(Number,Name,Capital)