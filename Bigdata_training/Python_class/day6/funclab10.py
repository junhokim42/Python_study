from random import *

def get_min_max(li):
    tup = (min(li), max(li))
    return tup

list_v = []
for i in range(10):
    list_v.append(randint(1, 30))

v = get_min_max(list_v)

min_v = min(v)
max_v = max(v)

print(f'생성된 리스트:{list_v}')
print(f'최소값은 {min_v}이고 최대값은 {max_v}입니다.')

