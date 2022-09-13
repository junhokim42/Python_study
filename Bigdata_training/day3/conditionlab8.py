from random import *

oper_num = randint(1, 10)
a=300
b=50
if oper_num == 1 or oper_num == 6:
    cal = a+b
elif oper_num == 2 or oper_num == 7:
    cal = a-b
elif oper_num == 3 or oper_num == 8:
    cal = a*b
elif oper_num == 4 or oper_num == 9:
    cal = a/b
else:
    cal = a%b

print('랜덤추출값:', oper_num, ', 결과값:', cal)