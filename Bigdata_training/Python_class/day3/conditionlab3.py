from random import *
grade = randint(1, 6)
if grade != 4 and grade != 5 and grade != 6:
    print(grade, '학년은 저학년입니다.')
else:
    print(grade, '학년은 고학년입니다.')