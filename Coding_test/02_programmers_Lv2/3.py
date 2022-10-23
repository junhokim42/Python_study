# 올바른 괄호
from collections import deque
def solution(s):
    answer = True
    check=0
    que =deque(s) 
    while(que):
        gawlho = que.popleft()
        if gawlho == "(" :
            check+=1
        else :
            check-=1
        if check < 0 :
            answer = False
            break 
    if check > 0 :
        answer = False
    return answer 