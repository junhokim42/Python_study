# 이진 변환 반복하기
def solution(s):
    answer = []
    count = 0
    count_eliminatedZero = 0
    
    while(s != '1'):
        count_eliminatedZero += len(s)-len(s.replace('0', ''))
        s = s.replace('0', '')
        s= bin(len(s))
        s = s[2:]
        count += 1
    
    answer.append(count)
    answer.append(count_eliminatedZero)
    
    return answer