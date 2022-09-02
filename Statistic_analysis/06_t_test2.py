import pandas as pd
from scipy import stats
import numpy as np
df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')

# Independent t-test
no_claim = df[df.클레임접수여부 == 0]
df2 = np.array(no_claim.방문빈도)

claim = df[df.클레임접수여부 == 1]
df3 = np.array(claim.방문빈도)

# print(stats.bartlett(df2, df3))

# print(stats.ttest_ind(df2, df3, equal_var = False))
# print('클레임 접수여부(0) 고객 평균방문빈도:', no_claim.방문빈도.mean())
# print('클레임 접수여부(1) 고객 평균방문빈도:', claim.방문빈도.mean())


# Two sample t-test
print(stats.ttest_rel(df['멤버쉽_프로그램_가입후_만족도'],df['멤버쉽_프로그램_가입전_만족도']))