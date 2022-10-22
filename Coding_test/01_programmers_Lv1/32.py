# 이상한 문자 만들기
def solution(s):
    word = s.split(' ')
    for i in range(len(word)):
        a=''
        for j in range(len(word[i])):
            if j%2 == 0:
                a += word[i][j].upper()
            else:
                a += word[i][j].lower()
        word[i] = a
                
    answer = ' '.join(word)
    return answer