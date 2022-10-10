# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    while(n//10 > 0):
        answer.append(n%10)
        n = n//10
    
    answer.append(n)
        
    return answer