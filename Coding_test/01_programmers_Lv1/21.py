# 수박수박수박수박수박수?
def solution(n):
    answer = ''
    subak = '수박'
    answer += (subak*(n//2) + subak[:-n%2])
    return answer