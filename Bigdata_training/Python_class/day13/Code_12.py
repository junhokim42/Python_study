import random

def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary), 1):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

before = [random.randint(50, 200) for _ in range(8)]
after = []

print('정렬 전 ->', before)

for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])


print('정렬 후 ->', after)