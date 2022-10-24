# 짝지어 제거하기

def solution(s):
    count = 0
    sentence = s
    
    while(len(s) > 1):
        a = count
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                sentence = sentence.replace(s[i-1]*2,'')
                count += 1
        s = sentence
        if a == count:
            print('end of iteration')
            break
    if sentence == '':
        answer = 1
    else:
        answer = 0

    return answer