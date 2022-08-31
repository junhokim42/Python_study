from ast import increment_lineno
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

groupby_purchasestyle = df.groupby('구매유형')
groupby_purchasestyle.describe()

labels = ['1','2','3','4']
sizes=[43,317,144,496]
colors=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('구매 유형에 따른 고객 분포')
plt.show()