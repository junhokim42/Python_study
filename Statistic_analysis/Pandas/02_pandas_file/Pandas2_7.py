import pandas as pd

data = {'name' : ['Jerry', 'Riah', 'Paul'],
        'algol' : ["A", "B", "C"],
        'basic' : ["C", "B", "B+"],
        'C++' : ["B+", "C", "C+"]}

df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)

df.to_csv("./df_sample.csv")