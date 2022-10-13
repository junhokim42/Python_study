import pandas as pd
import numpy as np
import seaborn as sns

# 1-21
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))

# 1-22
student1 = pd.Series({'국어':100, '영어': 80, '수학':90})
student2 = pd.Series({'국어':80, '영어': 90, '수학':80})

print(student1)
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print(type(division))
print('\n')

result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

# 1-23

student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

print(student1)
print(student2)
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print(type(division))
print('\n')

result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)


#1-24
student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90})

sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

# 1-25

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.head())
print('\n')
print(type(addition))

# 1-26
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail())
print('\n')
print(type(df))

addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))

subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))