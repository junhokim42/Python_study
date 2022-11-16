from random import *

def print_gugudan(num):
    if type(num) != int:
        return
    else:
        if 1<= num <= 9:
            for i in range(9):
                print('{} x {} = {}'.format(num, i+1, (i+1)*num))
        else:
            return
    return

rand_int = randint(0, 11)
print_gugudan(rand_int)