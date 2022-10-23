# 다음 큰 숫자
def solution(n):
    answer = 0
    a = -1
    num_one = len(bin(n)) - len(bin(n).replace('1', ''))
    while (num_one != a):
        n += 1
        a = len(bin(n)) - len(bin(n).replace('1', ''))
    
    answer = n
    return answer