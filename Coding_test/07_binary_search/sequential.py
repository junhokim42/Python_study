def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print('Enter the number of elements and press space for setence to find ')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('Enter the string in list. Split is according to space key')
array = input().split()

print(sequential_search(n, target, array))