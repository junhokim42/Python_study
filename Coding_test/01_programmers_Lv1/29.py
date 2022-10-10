# 직사각형 별찍기
a, b = map(int, input().strip().split(' '))
c = ''
for i in range(b):
    for j in range(a):
        c += '*'
    c += '\n'

print(c)