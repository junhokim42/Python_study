# 카펫

def solution(brown, yellow):
    answer = []
    for x in range(3, (brown + yellow)//2):
        if yellow % (x-2) == 0 and (brown + yellow) % x == 0:
            if yellow == (x-2)*((brown + yellow)//x-2):
                answer = [max(x, (brown + yellow)//x), min(x, (brown + yellow)//x)]
                break
    
    return answer

# x*y = brown + yellow
# (x-2)*(y-2) = yellow