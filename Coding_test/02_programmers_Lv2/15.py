# 멀리 뛰기

def solution(n):
    i = 1
    j = 1
    for _ in range(n-1):            
        i, j = j, i+j
    answer = j%1234567
    
    return answer