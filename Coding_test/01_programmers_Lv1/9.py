# 정수 내림차순으로 배치하기
def solution(n):
    
    str_list = list(str(n))

    str_list.sort()
    str_list.reverse()
    answer = int(''.join(str_list))
    
    return answer