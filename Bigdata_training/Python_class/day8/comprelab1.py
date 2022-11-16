def create_list(*arg, type = 1):
    if arg == None:
        result = [i for i in range(30)]
    elif type == 2:
        print(arg)
        result = [i for i in arg if i%2 == 0]
    elif type == 3:
        result = [i for i in arg if i%2 == 1]
    elif type == 4:
        result = [i for i in arg if i > 10]
    elif type == 1:
        result = [i for i in arg]
    return result

print(create_list(1, 2, 3, 10, 14, type = 2))
print(create_list(1, 2, 3, 10, 14, type = 3))
print(create_list(1, 2, 3, 10, 14, type = 4))
print(create_list(1, 2, 3, 10, 14, type = 1))
    