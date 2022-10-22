# 3진법 뒤집기
def solution(n):
    answer = 0
    sam = ''
    while(n>0):
        a = str(n%3)
        n = n//3
        sam += a
    for i in range(len(sam)):
        answer += 3**(len(sam)-i-1)*int(sam[i])
        
    return answer