import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

priceData = pd.read_csv("Ether 1 2.csv")
#total_pri = priceData["High"] + priceData["Low"]
aver_pri = priceData['Price']
exc_volume = priceData['exchange']
total_vol = priceData["TotalVol"]
chipData = DataFrame(np.linspace(0, 1499, 1500), columns=['Chip'])


lastTradeDate = str(priceData['TradeDate'][1])
chipData[lastTradeDate] = 0
total_volume = 60315969
chipData.loc[0, lastTradeDate] = 60315969 / total_volume       #上市之前的货币总量

trade_num = len(priceData)


for n in range(2,trade_num):
    newTradeDate = str(priceData['TradeDate'][n])
    chipData[newTradeDate] = chipData[lastTradeDate]
    turnover = exc_volume[n] / total_vol[n-1]
    chipData[newTradeDate] = chipData[newTradeDate] * (1 - turnover)
    seqChip = int(aver_pri[n] * 1)
    chipData.loc[seqChip, newTradeDate] += exc_volume[n] / total_vol[n]
    lastTradeDate = newTradeDate

chipData.to_csv("Result.csv")


result = pd.read_csv("Result.csv")
li = result.columns

for x in range(1000,1048):
    plt.bar(result['Chip'], result[li[x + 1]], width=0.1, ec='r', ls='-', lw=0.5, fc='b')
    plt.title(li[x + 1])
    plt.savefig("Pic_"+str(x))