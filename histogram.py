from ast import increment_lineno
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

plt.hist(df['서비스_만족도'], alpha=0.4, bins=7, rwidth=1, color='red', label='서비스만족도')

plt.legend()
plt.grid()
plt.xlabel('서비스만족도')
plt.ylabel('빈도')
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()