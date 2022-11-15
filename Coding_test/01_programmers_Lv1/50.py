# 신규 아이디 추천

import re

def solution(new_id):

    answer = step1(new_id)

    return answer

def step1(id):
    return step2(id.lower())

def step2(id):
    return step3(re.sub(r'[^\w\s\.\-\_]', '', id))

def step3(id):
    c = 0
    id = list(id)
    for i in range(len(id)):
        if (id[i] == '.') and (c==0):
            c += 1
        elif (id[i] == '.') and (c>=1):
            id[i] = ''
            c += 1
        elif id[i] != '.': 
            c = 0 
    return step4(''.join(id))

def step4(id):
    if id[0] == '.': start = 1
    else: start = 0

    if id[-1] == '.': answer = id[start:-1]
    else: answer = id[start:]

    return step5(answer)

def step5(id):
    if len(id) == 0:
        id = 'a'
    return step6(id)

def step6(id):
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == '.':
            id = id[:14]
    return step7(id)

def step7(id):
    if len(id) < 3:
        last = id[-1]
        while len(id) < 3:
            id += last
    return id