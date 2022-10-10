# 정수 제곱근 판별
def solution(n):
    answer = 0
    
    for i in range(2,n+2):
        if n == 1:
            answer = 4
            break
        if n%i == 0:
            if n//i == i:
                answer = (i+1)**2
                break
    
    if answer == 0:
        answer = -1
            
    return answer