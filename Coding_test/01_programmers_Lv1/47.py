# 소수 만들기
 
from itertools import *

sum_list = set()

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    a = list(combinations(nums, 3))
    for i in range(len(a)):
        if is_prime_number(sum(a[i])) == True:
            answer += 1
        
    return answer