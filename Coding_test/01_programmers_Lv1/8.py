# 하샤드 수
def solution(x):
    answer = True
    divide_num = 0
    list_x = list(str(x))
    
    for i in range(len(list_x)):
        divide_num += int(list_x[i])
        
    if x%divide_num != 0:
        answer = False
    
    return answer