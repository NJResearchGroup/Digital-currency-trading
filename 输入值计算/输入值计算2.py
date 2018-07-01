##计算CYQK_C、ASR、CKDW、PRP)##

import pandas as pd

priceData1 = pd.read_csv("Re.csv")
date = list(priceData1.columns)              #从2开始是第一个日期2015.8.10，应该是1046个日期，list里有1048个
priceData2 = pd.read_csv("Ether.csv")
aver_price = priceData2['Price']                  #从1开始是第一个价格，第0个价格是2018.8.9的，一共1047个

CYQK_C = {}
ASR = {}
CKDW = {}
PRP = {}
num = len(aver_price)
for n in range(2, num):
    dat = date[n+1]
    index_pri = int(aver_price[n])
    CYQK_C[dat] = priceData1[dat][0:index_pri].sum()
    start = int(aver_price[n]*0.9)
    end = int(aver_price[n]*1.1)
    ASR[dat] = sum(priceData1[dat][start:end+1])
    min = int(priceData1[priceData1[dat] != 0].index[0])
    for i in reversed(range(1, num)):
        if priceData1[dat][i] > 0:
            max = int(priceData1[dat][i].size)
    mean = sum(priceData1[dat].index * priceData1[dat])
    CKDW[dat] =(mean - min)/(max - min)
    PRP[dat] = (aver_price[n] - mean) / mean

print(CYQK_C)
print(ASR)
print(CKDW)
print(PRP)
