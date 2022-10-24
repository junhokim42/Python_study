# 구명보트

from collections import deque
def solution(people, limit):
    answer = 0
    list = deque(sorted(people))

    while(len(list) > 0):
        if len(list) == 1:
            answer += 1
            break
        elif list[0] + list[-1] <= limit:
            list.pop()
            list.popleft()
        else:
            list.pop()
        answer += 1

    return answer