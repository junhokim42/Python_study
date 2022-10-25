# 숫자 문자열과 영단어

def solution(s):
    sol = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
          'seven':7, 'eight':8, 'nine':9}
    for i in sol.keys():
        if i in s:
            # print(i)
            # print(sol.get(i))
            s = s.replace(i, str(sol.get(i)))
    answer = int(s)            

    return answer