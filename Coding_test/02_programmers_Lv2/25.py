# 연속 부분 수열 합의 개수

def solution(elements):
    res = set()
    data_len = len(elements)
    elements = elements*2
    for i in range(data_len):
        for j in range(data_len):
            res.add(sum(elements[j:j+i+1]))

    return len(res)