import pandas as pd

df = pd.read_csv('.\Statistic_analysis\pythondata\data\Ashopping.csv', sep=',', encoding='CP949')

# 10 of sample random selection
data_temp = df.sample(n=10, replace=False, random_state=123)
print(df)

# Select sample has specific condition
Churn_customer = df[df.이탈여부==1]
## print(Churn_customer.head())

# Field selection
df_1 = df[['고객ID', '방문빈도']]
## print(df_1.tail())

# Division for upper 500 and under 500
Under_500 = df[df.고객ID<=500]
Upper_500 = df[df.고객ID>500]
# print(Upper_500.head())

rawdata = open('.\Statistic_analysis\pythondata\data\Ashopping.csv', 'rb').read()
result = chardet.detect(rawdata)
charenc = result['encoding']
charenc