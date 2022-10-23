# 피보나치 수
def solution(n):
    i = 0
    j = 1
    for _ in range(n-1):            
        i, j = j, i+j
    answer = j%1234567
    
    return answer