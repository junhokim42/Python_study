# 두 개 뽑아서 더하기

from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        answer.append(sum(i))
        
    answer = list(set(answer))
    answer.sort()
    
    return answer