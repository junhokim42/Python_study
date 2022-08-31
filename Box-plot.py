import pandas as pd
import matplotlib
import seaborn as sns


# coding=cp949
df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False

sns.boxplot(x='성별', y='총 할인 금액', hue='성별', data=df)