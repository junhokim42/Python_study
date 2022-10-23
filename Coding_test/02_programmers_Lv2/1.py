# 최댓값과 최솟값
def solution(s):
    answer = ''
    s = s.split()
    s = list(map(int, s))
    s.sort()
    answer = str(s[0]) + ' ' + str(s[-1])
    return answer