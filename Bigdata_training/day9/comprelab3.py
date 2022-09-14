def mycompredict(**args):
    return {'my'+key:value for key, value in args.items()}

a= mycompredict(a=1, b=2, c=3, d=4)
b= mycompredict(apple = 6, student = 'Kim', date = ['06/14', '08/30'])
c= mycompredict()

print(a)
print(b)
print(c)
