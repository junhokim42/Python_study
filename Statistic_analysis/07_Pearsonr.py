import pandas as pd
from pingouin import partial_corr
from scipy import stats
df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')
df1 = df[['총_매출액','방문빈도','구매_카테고리_수']]

# print(df1.corr(method = 'pearson'))
print(partial_corr(data=df1, x ='총_매출액', y='방문빈도', covar='구매_카테고리_수'))

# print(stats.pearsonr(df1.총_매출액,df1.방문빈도))
# print(stats.pearsonr(df1.총_매출액, df1.구매_카테고리_수))
# print(stats.pearsonr(df1.방문빈도,df1.구매_카테고리_수))