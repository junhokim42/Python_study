import pandas as pd

df1 = pd.read_excel('./남북한발전전력량.xlsx')
df2 = pd.read_excel('./남북한발전전력량.xlsx', header = None)

print(df1)
print('\n')
print(df2)