# 최솟값 만들기
def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    B.reverse()
    for i in range(len(A)):
        answer += A[i] * B[i]
    

    return answer