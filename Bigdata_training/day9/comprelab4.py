from random import *

listv = set()
while len(listv) <10:
    listv.add(randint(1,100))

list_data = list(listv)
list_dict = {}
for i in range(10):
    list_dict[i] = list_data[i]

print(list_dict)
grades = {key: 'pass' if value >= 60 else 'nopass' for key, value in list_dict.items()}
print(grades)