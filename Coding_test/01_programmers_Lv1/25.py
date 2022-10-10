# 문자열 다루기 기본
def solution(s):
    answer = False
    if len(list(s)) in [4, 6]:
        try:
            print(int(s))
            answer = True
        except ValueError:
            pass
    return answer