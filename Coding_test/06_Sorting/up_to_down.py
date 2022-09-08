n = int(input('Enter # of number: '))
array = []
for i in range(n):
    array.append(int(input('Enter number in array: ')))

array = sorted(array, reverse = True)

for i in array:
    print(i, end=' ')
