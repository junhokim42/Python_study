# K번째수

def solution(array, commands):
    answer = []
    for i in commands:
        new = array[i[0]-1:i[1]]
        new.sort()
        answer.append(new[i[2]-1])
        
    return answer