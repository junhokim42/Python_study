def mydict(**args):
    dic = {}
    for key, value in args.items():
        key = 'my ' + key
        dic[key] = value
    return dic


a= mydict(a=1, b=2, c=3, d=4)
b= mydict(apple = 6, student = 'Kim', date = ['06/14', '08/30'])
c= mydict()

print(a)
print(b)
print(c)
