import random

def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]):
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    
    return ary

dataAry = [random.randint(50, 200) for _ in range(8)]
after = []

print('정렬 전 ->', dataAry)

dataAry = selectionSort(dataAry)

print('정렬 후 ->', dataAry)