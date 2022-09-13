from random import *

def print_triangle_withdeco(var, deco = '%'):
    if var == 2:
        for i in range(var):
            print(' '*(var-i-1) + deco*(i+1))
    elif var == 5 and deco == '*':
        for i in range(var):
            print(' '*(var-i-1) + deco*(i+1))
    else:
        for i in range(5):
            print(' '*(4-i) + '%'*(i+1))    

num = randint(1,10)
deco = choice(['*', '%', '$'])
print('num = {}'.format(num))
print('deco = {}'.format(deco))

print('num, deco 모두 넣었을 때 결과:')
print_triangle_withdeco(num, deco)
print('num만 넣었을 때 결과:')
print_triangle_withdeco(num)