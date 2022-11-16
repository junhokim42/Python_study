def myprint(*p, **args):
    if p == () and args == {}:
        print('Hello Python')
        return
    b = []

    for i in p:
        b.append(str(i))

    if args == {}:
        a = ','.join(b)
        print(f'**{a}**')

    else:
        for value in args.values():
            if 'sep' in args.keys():
                a = args['sep'].join(b)
                if value != args['sep']:
                    c = f'{value}{a}{value}'
            else:
                a = ','.join(b)
                c = f'{value}{a}{value}' 

        print(c)
        

myprint(10, 20, 30, deco = '@', sep = '-')
myprint('python', 'javascript', 'R', deco = '$')
myprint('가', '나', '다')
myprint(100)
myprint(True, 111, False, 'abc', deco = '&', sep = '')
myprint()