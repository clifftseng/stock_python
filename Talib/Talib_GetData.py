# 匯入套件
from haohaninfo import GOrder
import numpy as np

def GetKBar(Num,Prod,Kind,DN):
    # 取歷史報價
    Data = GOrder.GetHistoryKBar(Num,Prod,Kind,DN)
    # 刪除換行符號並依逗號分隔
    Data = [ i.strip('\n').split(',') for i in Data ]
    # 將資料改為Talib套件適用的格式
    KBar = {}
    KBar['date'] = np.array([ i[0] for i in Data ])
    KBar['open'] = np.array([ float(i[2]) for i in Data ])
    KBar['high'] = np.array([ float(i[3]) for i in Data ])
    KBar['low'] = np.array([ float(i[4]) for i in Data ])
    KBar['close'] = np.array([ float(i[5]) for i in Data ])
    KBar['volume'] = np.array([ float(i[6]) for i in Data ])
    return KBar
    