import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower','weight',
            'acceleration', 'model year', 'origin', 'name']

print(df.head())
print('\n')
print(df.tail())

print(df.shape)
print(df.info())

print(df.describe())
print('\n')
print(df.describe(include = 'all'))