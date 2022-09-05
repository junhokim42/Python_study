from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2002-09-05')
sec_dpc = (sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
sec_dpc_cs = sec_dpc.cumsum()

import matplotlib.pyplot as plt
plt.plot(sec.index, sec_dpc_cs, 'b', label = 'Samsung Electronics')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc = 'best')
plt.show()