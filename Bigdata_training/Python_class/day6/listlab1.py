from random import *

listnum = []
for i in range(10):
    listnum.append(randint(1, 50))

print('최초 listnum:')
print(listnum)

for i in range(len(listnum)):
    if listnum[i] < 10:
        listnum[i] = 100

print('10보다 작은 listnum 변수 100으로 변환:')
print(listnum)

print('listsum 첫번째 데이터:')
print(listnum[0])

print('listsum 마지막 데이터:')
print(listnum[-1])

print('listsum 2 ~ 6번째 데이터:')
print(listnum[1:6])

print('listsum 역순 정렬:')
print(listnum[::-1])

del listnum[4]

print('listsum 5번째 데이터 삭제:')
print(listnum)

print('listsum 모두 출력 (Slicing)')
print(listnum[0:len(listnum)])

del listnum[1:3]

print('listsum 2 ~ 3번째 데이터 삭제')
print(listnum)

print('listsum 모두 출력 (Slicing)')
for i in range(len(listnum)):
    print(listnum[i])
