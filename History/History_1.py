from haohaninfo import GOrder   # 匯入模組


# ---------------------------------股票---------------------------------------
StkProd = '2330'
StkData = GOrder.GetHistoryKBar('100', StkProd, 'Stock', '1')   # 取歷史報價
data = '\n'.join(StkData)         # 將List格式用換行符號合併為String格式
file = open(StkProd + '.csv','w') # 建立Excel檔案
file.write(data)                  # 儲存資料


# ---------------------------------期貨---------------------------------------
FutProd = 'TXF'
FutData = GOrder.GetHistoryKBar('100', FutProd, 'Future', '1')  # 取歷史報價
data = '\n'.join(FutData)         # 將List格式用換行符號合併為String格式
file = open(FutProd + '.csv','w') # 建立Excel檔案
file.write(data)                  # 儲存資料
