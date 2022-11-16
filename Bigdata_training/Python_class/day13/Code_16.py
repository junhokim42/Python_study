# 합계
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num-1)

print(addNumber(5))

# 팩토리얼
factValue = 1
for n in range(10, 0, -1):
    factValue *= n
print("10*9*...*1 = ", factValue)

def factorial(num):
    if num <= 1:
        print('1 반환')
        return 1
    print("%d*%d! 호출"%(num, num-1))

    retVal = factorial(num-1)

    print("%d*%d!(=%d) 반환"%(num, num-1, retVal))
    return num*retVal

print('\n5!= ', factorial(5))