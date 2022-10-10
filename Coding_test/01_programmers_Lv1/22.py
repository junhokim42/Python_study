# 가운데 글자 가져오기
def solution(s):
    answer = ''
    answer += s[len(s)//2-((len(s)-1)%2):len(s)//2+1]
    return answer