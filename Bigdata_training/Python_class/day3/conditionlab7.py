num = input('1부터 10 사이의 숫자를 하나 입력하세요 : ')
num = int(num)
if num < 1 or num > 10:
    print('1부터 10 사이의 값이 아닙니다.')
elif num %2 ==1 :
    print(num, ': 홀수')
else:
    print(num, ': 짝수')