# for item in range(2,20):
#     for each in range(2,20):
#         print(item, 'X', each, '=', item*each)

# y=lambda x:3*x
# print(y(12))

# add=lambda a,b:a+b
# print(add(2,3))

# a=input('Enter number')
# a=float(a)
# print(a*3)

def service_price():
    service = input('Enter service, a/b/c: ')
    valueAdded = input("Contain tax? y/n: ")
    if valueAdded == 'y':
        if service =='a':
            result = 23*1.1
        if service == 'b':
            result = 40*1.1
        if service == 'c':
            result = 67*1.1
    if valueAdded == 'n':
        if service =='a':
            result = 23
        if service == 'b':
            result = 40
        if service == 'c':
            result = 67
    print(round(result,1))

service_price()