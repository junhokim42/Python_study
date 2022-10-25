# 최소직사각형

def solution(sizes):
    answer = 0
    sorted_sizes = []
    for i in range(len(sizes)):
        a = sorted(sizes[i])
        sorted_sizes.append(a)
    
    a = []
    b = []
    for i in range(len(sorted_sizes)):
        a.append(sorted_sizes[i][0])
        b.append(sorted_sizes[i][1])

    answer = max(a)*max(b)
    
    return answer