from random import *

set1 = set()
while len(set1) < 6:
    set1.add(randint(1,45))

print(f'행운의 로또번호: {str(set1)[1:len(str(set1))-1]}')
print('행운의 로또번호:', end='')
print(*set1, sep = ',')