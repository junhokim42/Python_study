from random import *

pairNum1 = randint(1, 6)
pairNum2 = randint(1, 6)

while pairNum1 != pairNum2:
    print ('pairNum1 = ', pairNum1, 'pairNum2 = ', pairNum2)
    if pairNum1 > pairNum2:
        print('{}이 {}보다 크다'.format(pairNum1, pairNum2))
    else:
        print('{}이 {}보다 작다'.format(pairNum1, pairNum2))
    pairNum1 = randint(1, 6)
    pairNum2 = randint(1, 6)

print ('pairNum1 = ', pairNum1, 'pairNum2 = ', pairNum2)
print("게임끝")