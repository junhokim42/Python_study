import pandas as pd
import numpy as np
from scipy import stats
df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding = 'CP949')

X = pd.crosstab(df.클레임접수여부, df.구매유형, margins = True)
# print(X)

Ob = X.values[1,:4]
Pr = np.array([0.1, 0.3, 0.2, 0.4])
n = X.values[1, 4]
E = n*Pr
print(stats.chisquare(Ob, E))