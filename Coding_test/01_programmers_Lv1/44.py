# 폰켓몬

def solution(nums):
    a = len(nums)//2
    b = len(set(nums))
    answer = min(a, b)
    return answer