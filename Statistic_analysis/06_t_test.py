import pandas as pd
from scipy import stats

df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')

print('총매출액 평균: ', df.총_매출액.mean())
print(stats.ttest_1samp(df['총_매출액'], 7040000))