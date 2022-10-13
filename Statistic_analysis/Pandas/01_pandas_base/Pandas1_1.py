from multiprocessing.dummy import Array
import pandas as pd

# 1-1
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)
print('\n')

# 1-2
idx = sr.index
val = sr.values
print(idx)
print(val)
print('\n')

# 1-3
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr)
print(sr[0])
print(sr['이름'])
print('\n')
print(sr[[1,2]])
print(sr[['생년월일', '성별']])
print('\n')
print(sr[1:2])
print(sr['생년월일':'성별'])

#1-4
dict_data = {'c0': [1, 2, 3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3': [10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data)

print(type(df))
print(df)

#1-5
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns=['나이', '성별', '학교'])

print(df)
print(df.index)
print(df.columns)

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df)
print(df.index)
print(df.columns)

# 1-6
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns = ['나이', '성별','학교'])
print(df)
print('\n')

df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True)
print(df)
print('\n')

# 1-7
exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

df3 = df[:]
df3.drop(['우현','인아'], axis=0, inplace=True)
print(df3)
print('\n')

# 1-8
exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

#1-9
exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}
df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

labell = df.loc['서준']
position1 = df.iloc[0]
print(labell)
print(position1)
print('\n')

label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0, 1]]
print(label2)
print(position2)
print('\n')

label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3)
print(position3)
print('\n')

# 1-10
exam_data = {'이름': ['서준', '우현', '인아'],
            '수학' : [90, 80, 70],
            '영어' : [89, 38, 49],
            '음악' : [85, 34, 90],
            '체육' : [48, 39, 50]}

df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

english = df.영어
print(english)
print(type(english))

music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2))

# 1-11
## 1개 원소 선택
exam_data = {'이름': ['서준', '우현', '인아'],
            '수학' : [90, 80, 70],
            '영어' : [89, 38, 49],
            '음악' : [85, 34, 90],
            '체육' : [48, 39, 50]}

df = pd.DataFrame(exam_data)
df.set_index('이름', inplace = True)
print(df)

a = df.loc['서준', '음악']
print(a)
b = df.iloc[0, 2]
print(b)

##2개 이상 원소 선택
c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0, [2,3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0,2:]
print(f)

##2개 이상 원소 선택 (데이터프레임)
g= df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
h = df.iloc[[0,1], [2,3]]
print(h)
i = df.loc['서준':'우현', '음악':'체육']
print(i)
j = df.iloc[0:2, 2:]
print(j)

# 1-12
exam_data = {'이름': ['서준', '우현', '인아'],
            '수학' : [90, 80, 70],
            '영어' : [89, 38, 49],
            '음악' : [85, 34, 90],
            '체육' : [48, 39, 50]}

df = pd.DataFrame(exam_data)
df['국어'] = 80
print(df)

#1-13
df.loc[3] = 0
print(df)

df.loc[4] = ['동규', 67, 89, 34, 12, 89]
print(df)

df.loc['행5'] = df.loc[3]
print(df)

# 1-14
exam_data = {'이름': ['서준', '우현', '인아'],
            '수학' : [90, 80, 70],
            '영어' : [89, 38, 49],
            '음악' : [85, 34, 90],
            '체육' : [48, 39, 50]}

df = pd.DataFrame(exam_data)

df.set_index('이름', inplace = True)
print(df)
print('\n')

df.iloc[0][3] = 80
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 50
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)
print('\n')

# 1-15
exam_data = {'이름': ['서준', '우현', '인아'],
            '수학' : [90, 80, 70],
            '영어' : [89, 38, 49],
            '음악' : [85, 34, 90],
            '체육' : [48, 39, 50]}

df = pd.DataFrame(exam_data)
df = df.transpose()
print(df)
print('\n')

df = df.T
print(df)

# 1-16
exam_data = {'이름': ['서준', '우현', '인아'],
            '수학' : [90, 80, 70],
            '영어' : [89, 38, 49],
            '음악' : [85, 34, 90],
            '체육' : [48, 39, 50]}

df = pd.DataFrame(exam_data)
ndf = df.set_index(['이름'])
print(ndf)
print('\n')
ndf2 = ndf.set_index(['음악'])
print(ndf2)
print('\n')
ndf3 = ndf.set_index(['수학', '음악'])
print(ndf3)

# 1-17
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3': [10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
print('\n')

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

ndf2 = df.reindex(new_index, fill_value = 0)
print(ndf2)

# 1-18
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3': [10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
print('\n')

ndf = df.reset_index()
print(ndf)

# 1-19
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3': [10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index = ['r0', 'r1', 'r2'])
print(df)
print('\n')

ndf = df.sort_index(ascending = False)
print(ndf)