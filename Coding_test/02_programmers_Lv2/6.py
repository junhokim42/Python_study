# 숫자의 표현
def solution(n):
    answer = 0
    x = 0
    count = 0
    a = 0
    
    while (x != n):
        x += 1
        answer += x
        if answer > n:
            answer = 0
            x = a+1
            a += 1
            continue
        elif answer == n:
            count += 1
            answer = 0
            x = a+1
            a += 1
            continue    
        
    return count