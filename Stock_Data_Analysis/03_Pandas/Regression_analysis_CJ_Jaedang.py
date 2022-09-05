import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

from scipy import stats
import matplotlib.pylab as plt

yf.pdr_override()

CJjaedang = pdr.get_data_yahoo('097950.KS', '2012-09-05')
CJjaedang_pre = pdr.get_data_yahoo('097955.KS', '2012-09-05')

# import matplotlib.pyplot as plt
# plt.figure(figsize = (9, 5))
# plt.plot(CJjaedang.index, CJjaedang.Close, 'r--', label='CJjaedang')
# plt.plot(CJjaedang_pre.index, CJjaedang_pre.Close, 'b', label='CJjaedang preferred stock')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

df = pd.DataFrame({'X': CJjaedang['Close'], 'Y': CJjaedang_pre['Close']})
df = df.fillna(method ='bfill')
df = df.fillna(method ='ffill')
regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f}*X + {regr.intercept:.2f}'

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope*df.X + regr.intercept, 'r')
plt.legend(['CJjaedang and CJjaedang preferred stock', regr_line])
plt.title([f'CJjaedang and CJjaedang preferred stock (R = {regr.rvalue:.2f})'])
plt.xlabel('CJjaedang stock price')
plt.xlabel('CJjaedang preferred stck price')
plt.show()