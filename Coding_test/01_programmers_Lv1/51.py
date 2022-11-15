# 숫자 짝꿍

def solution(X, Y):
    answer = ''
    X = list(X)
    Y = list(Y)
    
    a = ['9', '8', '7', '6', '5', '4', '3', '2', '1' ,'0']
    for i in range(len(a)):
        for j in range(min(X.count(a[i]), Y.count(a[i]))):
            answer += a[i]
    
    if answer == '':
        answer = '-1'
        
    while answer[0] == '0' and len(answer) > 1:
        answer = answer[1:]
    
    return answer