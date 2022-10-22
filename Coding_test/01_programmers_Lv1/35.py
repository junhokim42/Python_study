# 시저 암호
def solution(s, n):
    answer = ''

    for i in range(len(s)):
        if (ord(s[i]) > 96):
            if (ord(s[i])+n > 122):
                answer += chr(ord(s[i])+n-26)
            else:
                answer += chr(ord(s[i])+n)
        elif(ord(s[i]) == 32):
             answer += ' '
        else:
            if (ord(s[i])+n > 90):
                answer += chr(ord(s[i])+n-26)
            else:
                answer += chr(ord(s[i])+n)

    return answer