dic = {'월': (27, 19), '화':(26, 19), '수':(29,15),
'목':(29,17), '금':(31,16), '토':(29,18),'일':(18,19)}
enter = input('요일명을 한글로 입력하세요:')
if enter in dic:
    print(f'{enter}요일의 최저온도는 {str(dic[enter][1])}이고 최고 온도는 {str(dic[enter][0])}입니다')
else:
    print(f'{enter}요일의 정보를 찾을 수 없습니다')

