# 나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    while(True):
        if n%(answer+2) == 1:
            break
        answer += 1
    
    return answer+2