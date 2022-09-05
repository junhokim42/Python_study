import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

from scipy import stats
import matplotlib.pylab as plt

yf.pdr_override()

npc = pdr.get_data_yahoo('004250.KS', '2002-09-05')
npc_pre = pdr.get_data_yahoo('004255.KS', '2002-09-05')

# import matplotlib.pyplot as plt
# plt.figure(figsize = (9, 5))
# plt.plot(npc.index, npc.Close, 'r--', label='NPC')
# plt.plot(npc_pre.index, npc_pre.Close, 'b', label='NPC preferred stock')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

df = pd.DataFrame({'X': npc['Close'], 'Y': npc_pre['Close']})
df = df.fillna(method ='bfill')
df = df.fillna(method ='ffill')
regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f}*X + {regr.intercept:.2f}'

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope*df.X + regr.intercept, 'r')
plt.legend(['NPC and NPC preferred stock', regr_line])
plt.title([f'NPC and NPC preferred stock (R = {regr.rvalue:.2f})'])
plt.xlabel('NPC stock price')
plt.xlabel('NPC preferred stck price')
plt.show()