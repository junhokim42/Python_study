# 제일 작은 수 제거하기
def solution(arr):
    print(arr.index(min(arr)))
    del(arr[arr.index(min(arr))])
    if arr == []:
        arr.append(-1)
    return arr