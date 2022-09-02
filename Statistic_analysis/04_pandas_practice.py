import pandas as pd
import numpy as np

# Series

series = pd.Series([1,2,3,4,5])
print(series)

# Sales Data

sales_data = {
    'Cosmetic': [300, 274, 150, 524, 211],
    'Cloth': [773, 657, 699, 324, 487],
    'F&B': [362, 131, 593, 348, 98],
    'Electronic': [458, 667, 123, 521, 662]
}

columns_list = ['Cosmetic', 'Cloth', 'F&B', 'Electronic']
index_list = ['2014', '2015', '2016', '2017', '2018']

df_sales=pd.DataFrame(data=sales_data, columns=columns_list, index=index_list)
print(df_sales)

# Statistical Info
print(df_sales.mean())
print(df_sales.std())
print(df_sales.mean(axis=1))
print(df_sales.describe())


# Department Store
dep_data ={
    'Myeongdong': [59060, 49296, 62015, 48621],
    'Bundang': [9312, 1267, 6893, 7226],
    'Gwangju': [2627, 4145, 4088, 4321],
    'Busan': [14211, 11071, 11234, 15424]
}

col_list=['Myeongdong', 'Bundang', 'Gwangju', 'Busan']
index_list=['2011', '2012', '2013', '2014']

df_store=pd.DataFrame(dep_data, columns=col_list, index=index_list)

print(df_store)
print(df_store['Myeongdong']['2013':'2015'])