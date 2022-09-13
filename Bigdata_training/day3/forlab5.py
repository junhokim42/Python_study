from random import *
start = randint(1, 10)
end = randint(30, 40)
s=0
for i in range(start, end+1, 2):
    if i%2 == 0:
        s+=i
    else:
        s+=i+1

print('{}부터 {}까지의 짝수의 합: {}'.format(start, end, s))