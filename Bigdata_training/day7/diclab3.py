dic = {'myinfo' : {'number' : 1, 'emailaddr' : 'Bigdata123@naver.com', 'movie' : ['Inception', 'Source code'], 'food' : ['Hamburger', 'Kimchi']}}
for key, value in dic.items():
    for key_myinfo, value_myinfo in value.items():
        print(f'{key_myinfo} : {value_myinfo}')
