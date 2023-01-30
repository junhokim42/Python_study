# 귤고르기

from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = sorted(Counter(tangerine).items(), reverse=True, key=lambda x:x[1])
    for key, v in cnt:
        if k <=0:break
        k -=v
        answer += 1
    return answer