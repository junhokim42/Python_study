# 문자열 내림차순으로 배치하기
def solution(s):
    answer = ''
    a= list(s)
    a.sort(reverse = True)
    for i in range(len(a)):
        answer += ''.join(a[i])
    return answer