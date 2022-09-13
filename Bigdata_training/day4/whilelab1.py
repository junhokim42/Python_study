from random import *

a=1
nan = randint(5, 10)
print('nan:', nan)
while a < nan+1:
    print(a, '->', a**2)
    a += 1