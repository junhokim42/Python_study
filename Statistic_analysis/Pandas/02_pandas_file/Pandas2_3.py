import pandas as pd

df = pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)