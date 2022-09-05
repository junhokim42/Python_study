import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

from scipy import stats
import matplotlib.pylab as plt

yf.pdr_override()

nexen = pdr.get_data_yahoo('005720.KS', '2016-01-05')
nexen_pre = pdr.get_data_yahoo('005725.KS', '2016-01-05')

# import matplotlib.pyplot as plt
# plt.figure(figsize = (9, 5))
# plt.plot(nexen.index, nexen.Close, 'r--', label='Nexen')
# plt.plot(nexen_pre.index, nexen_pre.Close, 'b', label='Nexen preferred stock')
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()

df = pd.DataFrame({'X': nexen['Close'], 'Y': nexen_pre['Close']})
df = df.fillna(method ='bfill')
df = df.fillna(method ='ffill')
regr = stats.linregress(df.X, df.Y)
regr_line = f'Y = {regr.slope:.2f}*X + {regr.intercept:.2f}'

plt.figure(figsize=(7, 7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope*df.X + regr.intercept, 'r')
plt.legend(['Nexen and Nexen preferred stock', regr_line])
plt.title([f'Nexen and Nexen preferred stock (R = {regr.rvalue:.2f})'])
plt.xlabel('Nexen stock price')
plt.xlabel('Nexen preferred stck price')
plt.show()