# 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    for i in range(len(choices)):
        if choices[i] < 4:
            answer += survey[i][0]*(4-choices[i])
        elif choices[i] > 4:
            answer += survey[i][1]*(choices[i]-4)
    
    MBTI = ''
    if answer.count('R') >= answer.count('T'):
        MBTI += 'R'
    else:
        MBTI += 'T'

    if answer.count('C') >= answer.count('F'):
        MBTI += 'C'
    else:
        MBTI += 'F'
        
    if answer.count('J') >= answer.count('M'):
        MBTI += 'J'
    else:
        MBTI += 'M'
        
    if answer.count('A') >= answer.count('N'):
        MBTI += 'A'
    else:
        MBTI += 'N'
        
    return MBTI