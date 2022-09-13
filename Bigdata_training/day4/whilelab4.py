season = int(input('1~12 사이의 값을 입력하세요 : '))
while season >= 1 and season <= 12:
    if season in [12, 1, 2]:
        print('{}월은 겨울'.format(season))
    elif season in [3, 4, 5]:
        print('{}월은 봄'.format(season))
    elif season in [6, 7, 8]:
        print('{}월은 여름'.format(season))
    elif season in [9, 10, 11]:
        print('{}월은 가을'.format(season))
    season = int(input('1~12 사이의 값을 입력하세요 : '))
print('1~12 사이의 값을 입력하세요!')