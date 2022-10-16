import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower',
            'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.count())
print('\n')

print(type(df.count()))

unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')

print(type(unique_values))