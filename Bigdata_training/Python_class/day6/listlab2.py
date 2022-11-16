from random import *

lotto = []
while True:
    rand_int = randint(1,45)
    for i in range(6):
        if rand_int not in lotto:
            lotto.append(rand_int)
        if len(lotto) > 5:
            break
    if len(lotto) > 5:
            break

lotto.sort()
print('행운의 로또번호 : ', lotto)