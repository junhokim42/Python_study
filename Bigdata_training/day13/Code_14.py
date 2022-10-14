import random

def seqSearch(ary, fdata):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fdata:
            pos = i
            break
    return pos

dataAry = [random.randint(50, 200) for _ in range(8)]
findData = random.choice(dataAry)

print('배열 -> ', dataAry)
position = seqSearch(dataAry, findData)
if (position == -1):
    print(findData, '는 없어요')
else:
    print(findData, '는', position, '위치에 있음')