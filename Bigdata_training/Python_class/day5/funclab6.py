from random import *

def differtwovalue(num1, num2):
    return max(num1, num2) - min(num1, num2)

count = 0
while count <5:
    X = randint(1, 30)
    Y = randint(1, 30)
    result = differtwovalue(X, Y)

    print("{} 와 {}의 차는 {}입니다".format(X, Y, result))
    count += 1