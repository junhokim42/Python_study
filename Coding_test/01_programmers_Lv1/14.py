# 두 정수 사이의 합
def solution(a, b):
    answer = 0
    for i in range(min(a,b),max(a,b)+1):
        answer += i
    return answer