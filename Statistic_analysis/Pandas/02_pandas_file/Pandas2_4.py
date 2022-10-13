import pandas as pd

url = './sample.html'
tables = pd.read_html(url)

print(len(tables))

for i in range(len(tables)):
    print("table[%s]"%i)
    print(tables[i])
    print('\n')

df = tables[1]

df.set_index(['name'], inplace=True)
print(df)