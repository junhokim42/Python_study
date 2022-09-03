import pandas as pd
import numpy as np
from sklearn.cross_decomposition import CCA
from scipy import stats

df = pd.read_csv('.\Statistic_analysis\pythondata\data\CCA.csv', sep=',', encoding = 'CP949')
U = df[['품질','가격','디자인']]
V = df [['직원 서비스', '매장 시설', '고객관리']]
print(df.head())

cca = CCA(n_components=1).fit(U, V)
U_c, V_c = cca.transform(U, V)
U_c1 = pd.DataFrame(U_c)[0]
V_c1 = pd.DataFrame(V_c)[0]
print(U_c)
print('\n', V_c)

CC1 = stats.pearsonr(U_c1, V_c1)
print('제1정준상관계수:', CC1)

print('제품 만족도 정준변수와 해당 변수들간 정준적재량:', np.corrcoef(U_c1.T, U.T)[0,1:4])
print('제품 만족도 정준변수와 매장 만족도 변수들간 교차적재량:', np.corrcoef(U_c1.T, V.T)[0,1:])
print('매장 만족도 정준변수와 해당 변수들간 정준적재량:', np.corrcoef(V_c1.T, V.T)[0,1:])
print('매장 만족도 정준변수와 제품 만족도 변수들간 정준적재량:', np.corrcoef(V_c1.T, U.T)[0,1:4])
