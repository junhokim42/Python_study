from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

gc_pharma = pdr.get_data_yahoo('006280.KS', start='2002-09-05')
gc_pharma_dpc = (gc_pharma['Close'] - gc_pharma['Close'].shift(1)) / gc_pharma['Close'].shift(1) * 100
gc_pharma_dpc.iloc[0] = 0

import matplotlib.pyplot as plt

# # Stock chart plot
# plt.plot(gc_pharma.index, gc_pharma.Close, '#008000', label='GC Pharma Corporation')
# plt.legend(loc = 'best')
# plt.show()

#
plt.hist(gc_pharma_dpc, bins=30)
plt.grid(True)
plt.show()