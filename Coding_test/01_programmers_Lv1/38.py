# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    
    for i in strings:
        i = i[n] + i
        answer.append(i)
        
    answer_sort = sorted(answer)
    answer = []
    for i in answer_sort:
        answer.append(i[1:])
    
    return answer