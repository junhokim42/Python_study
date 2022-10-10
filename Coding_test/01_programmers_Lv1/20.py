# 없는 숫자 더하기
def solution(numbers):
    list_num = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numbers)):
        list_num.remove(numbers[i])
    
    answer = sum(list_num)
    
    return answer