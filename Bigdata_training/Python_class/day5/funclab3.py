def expr(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 / num2
    else:
        return None 


num1 = int(input('숫자 1: '))
num2 = int(input('숫자 2: '))
op = input('연산자: ')
result = expr(num1, num2, op)

if result == None:
    print('수행불가')
else:
    print('연산결과 : {}'.format(result))