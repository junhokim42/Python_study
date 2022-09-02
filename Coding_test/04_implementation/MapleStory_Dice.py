from random import *

b = True
while b:
    Luk = randint(4, 12)
    Dex = randint(4, 12)
    Str = randint(4, 12)
    Int = randint(4, 12)
    a = Luk + Dex + Str + Int
    while a != 25:
        Luk = randint(4, 12)
        Dex = randint(4, 12)
        Str = randint(4, 12)
        Int = randint(4, 12)
        a = Luk + Dex + Str + Int
    print('Str: {}\nDex: {}\nInt: {}\nLuk: {}'.format(Str, Dex, Int, Luk))
    if Int == 4 and Luk == 4:
        print("전사")
        b = False
    elif (Str == 4 or Dex == 4) and Int == 4:
        print("도적")
        b = False
    elif Dex == 4 and Int == 4:
        print("궁수")
        b = False
    elif Str == 4 and Dex == 4:
        print("법사")
        b = False
    else:
        print("주사위 다시 굴리기")
