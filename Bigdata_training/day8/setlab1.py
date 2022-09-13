from random import *

set1 = set()
set2 = set()

while len(set1) < 10:
    set1.add(randint(1,20))

while len(set2) < 10:
    set2.add(randint(1,20))

print(f'집합1:{set1}')
print(f'집합2:{set2}')
print(f'두 집합에 모두 있는 데이터:{set1&set2}')
print(f'집합1 또는 집합2에 있는 데이터:{set1.union(set2)}')
print(f'집합1에는 있고 집합2에는 없는 데이터:{set1 - set2}')
print(f'집합2에는 있고 집합1에는 없는 데이터:{set2 - set1}')
print(f'집합1과 집합2가 각자 가지고 있는 데이터:{set2^set1}')
