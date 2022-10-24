# N개의 최소공배수

def solution(arr):
    answer = 1
    while(True):
        count = 0
        for i in arr:
            if answer%i == 0:
                count +=1
        if count == len(arr):
            break    

        answer += 1

    return answer