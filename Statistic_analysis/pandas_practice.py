import pandas as pd
import numpy as np

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