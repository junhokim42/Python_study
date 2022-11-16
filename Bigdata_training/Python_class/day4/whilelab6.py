from math import factorial


num = int(input('숫자를 입력하세요 : '))
while True:
    if num == 0:
        print('종료')
        break
    elif num > 0:
        print('입력값:{}'.format(num))
        print(factorial(num))
        break
    elif num < 0:
        minus = str(num)
        num = int(minus[1:])
        print('입력값(부호변경):{}'.format(num))
        print(factorial(num))
        break
