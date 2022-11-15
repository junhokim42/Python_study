# H-Index

def solution(citations):
    answer = 0
    while True:
        count = 0
        for i in citations:
            if answer < i:
                count += 1
        if answer < count:
            answer += 1
        else:
            break
        
    return answer