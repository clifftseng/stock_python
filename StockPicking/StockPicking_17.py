from haohaninfo import MarketInfo

# 想要篩選的產業別
Target = '半導體'

# 公司基本資訊 (資訊代碼，股票標的)
Data = MarketInfo.GetMarketInfo('3001','All')

# 逐檔股票判斷
for i in Data:
    Number = i[0]   # 股票代碼
    Industry = i[1] # 產業別
    Name = i[2]     # 公司名稱
    
    # 該檔股票符合設定的產業別
    if Target in Industry:
        print(Number,Name)