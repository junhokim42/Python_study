from random import *

nan = randint(0, 30)
count = 0
while 1 < nan < 27:
    print(chr(nan+64) + '({})'.format(nan))
    nan = randint(0, 30)
    count += 1
print('수행횟수는 {}번입니다'.format(count))
