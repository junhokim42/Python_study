import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s)

s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8])
s.index.name = 'MY_IDX'
print(s)

ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
s = s.append(ser)
print(s)
print(s.index[-1])
print(s.values[-1])
print(s.loc[8.0])
print(s.iloc[-1])

print(s.describe())