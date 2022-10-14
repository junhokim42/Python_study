import random

def binSearch(ary, fdata):
    pos = -1
    start = 0
    end = len(ary) -1
    while (start <= end):
        mid = (start + end) // 2
        if (fdata == ary[mid]):
            pos = mid
            break
        elif (fdata > ary[mid]):
            start = mid + 1
        else:
            end = mid -1

    return pos

dataAry = [random.randint(50, 200000) for _ in range(8000)]
dataAry.sort()
findData = random.choice(dataAry)

# print('배열 ->', dataAry)
position = binSearch(dataAry, findData)
if (position == -1):
    print(findData, '는 없음')
else:
    print(findData, '는', position, '위치에 있음')