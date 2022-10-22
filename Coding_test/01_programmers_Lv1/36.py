# 1차 비밀지도
def solution(n, arr1, arr2):
    answer1 = []
    answer2 = []
    answer = ['#'*n]*n
    
    for i in range(n):
        answer1.append(bin(arr1[i])[-n:])
        answer2.append(bin(arr2[i])[-n:])
        
        while len(answer1[i]) < n:
            answer1[i] = '0' + answer1[i]
        
        while len(answer2[i]) < n:
            answer2[i] = '0' + answer2[i]
            
        answer1[i] = answer1[i].replace('b','0')
        answer2[i] = answer2[i].replace('b','0')

        for j in range(n):
            if answer1[i][j] == answer2[i][j] and answer2[i][j] == '0':
                answer[i] = answer[i][0:j] + ' ' + answer[i][j+1:]
    return answer