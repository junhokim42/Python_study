# 같은 숫자는 싫어
def solution(arr):
    stack = []
    result = [arr[0]]
    for num in arr:
        if stack:
            curr = stack.pop()
            if curr != num:
                result.append(num)

        stack.append(num)
    return result