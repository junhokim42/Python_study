# 약수의 개수와 덧셈
import math

def solution(left, right):
    answer = (left+right)*(right-left+1)//2 - 2*sum(i**2 for i in range(math.ceil(left**(1/2)),math.floor(right**(1/2))+1))
    
    return answer