import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

from scipy import stats
import matplotlib.pylab as plt

yf.pdr_override()

samsung = pdr.get_data_yahoo('005930.KS', '2005-09-05')
samsung_pre = pdr.get_data_yahoo('005935.KS', '2005-09-05')

# import matplotlib.pyplot as plt
# plt.figure(figsize = (9, 5))
# plt.plot(samsung.index, samsung.Close, 'r--', label='NPC')
# plt.plot(samsung_pre.index, samsung_pre.Close, 'b', label='NPC preferred stock')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

df = pd.DataFrame({'X': samsung['Close'], 'Y': samsung_pre['Close']})
df = df.fillna(method ='bfill')
df = df.fillna(method ='ffill')
regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f}*X + {regr.intercept:.2f}'

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope*df.X + regr.intercept, 'r')
plt.legend(['Samsung Electronic and Samsung Electronic preferred stock', regr_line])
plt.title([f'Samsung Electronic and Samsung Electronic preferred stock (R = {regr.rvalue:.2f})'])
plt.xlabel('Samsung Electronic stock price')
plt.xlabel('Samsung Electronic preferred stck price')
plt.show()