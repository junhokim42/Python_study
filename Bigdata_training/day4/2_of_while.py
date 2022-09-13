a=1
b=1
while a < 20:
    a += 2
    b += 1
    while b < 5:
        a += 2
        b += 1
        print('a: {}, b: {}'.format(a, b))
        if a > 5:
            print('Break inner Loop') # 여기를 outer Loop의 break로 설정해서 결과에 'Break inner Loop'가 출력되지 않게 하고 싶습니다.
            break
    print('a: {}, b: {}'.format(a, b))
    if b > 10:
        print('Break outer Loop') 
        break 
print('Complete')