from ast import increment_lineno
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))
# plt.show()

df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

df.plot.scatter(x='방문빈도', y='총_매출액', grid=True, title='방문 빈도와 총 매출액간 관계')
plt.show()