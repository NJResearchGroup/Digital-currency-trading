##计算ARC、VRC、SRC、KRC##

import pandas as pd

priceData = pd.read_csv("Ether.csv")
aver_price = priceData['Price']                  #从1开始是第一个价格，第0个价格是2018.8.9的，一共1047个
date = priceData['TradeDate']
tr = priceData['Turnover']

TR = [tr[1]]
ATR = [tr[1]]
ARC = []
VRC = []
SRC = []
KRC = []


total_num = len(aver_price)


for n in range(2, total_num):
    dat = date[1:n+1]
    pri = aver_price[1:n+1]
    RC = (aver_price[n] - pri) / aver_price[n]
    turnover = tr[n]
    ARC_ele = []
    for i in range(1, n):
        ATR[i-1] = TR[i-1] * (1 - tr[n])
        ARC_ele.append(ATR[i-1] * RC[i])

    atr_sum = sum(ATR)
    arc_sum = sum(ARC_ele)
    arc = arc_sum / atr_sum
    ARC.append(arc)
    ATR.append(turnover)
    TR = ATR
    VRC_ele = []
    SRC_ele = []
    KRC_ele = []
    for i in range(1,n):
        vrc_ele = ATR[i - 1] * ((RC[i] - arc)**2)
        VRC_ele.append(vrc_ele)
        src_ele = ATR[i - 1] * ((RC[i] - arc) ** 3)
        SRC_ele.append(src_ele)
        krc_ele = ATR[i - 1] * ((RC[i] - arc) ** 4)
        KRC_ele.append(krc_ele)
    vrc_sum = sum(VRC_ele)
    vrc = (n * vrc_sum) / ((n-1) * atr_sum)
    VRC.append(vrc)
    src_sum = sum(SRC_ele)
    src = (n * src_sum) / ((n-1) * (vrc ** 1.5) * atr_sum)
    SRC.append(src)
    krc_sum = sum(KRC_ele)
    krc = (n * krc_sum) / ((n - 1) * (vrc ** 2) * atr_sum)
    KRC.append(krc)


print(ARC)
print(VRC)
print(SRC)
print(KRC)


