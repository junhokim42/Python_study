from random import *

def print_triangle2(var):
    if 1 <= var <= 10:
        for i in range(var):
            print('@'*(var-i))
    else:
        pass

num = randint(1,10)
print('num = {}'.format(num))
print_triangle2(num)