dic = {'red':'#ff0000', 'blue':'#0000ff', 'yellow':'#ffff00', 
'orange':'#ffa500', 'black':'#000000', 'white':'#ffffff', 'violet':'#ee82ee',
'pink':'#ffc0cb', 'lime':'00ff00'}

enter = input('칼라명을 영문으로 입력하세요:')
if enter in dic:
    print(f'{enter} 칼라의 RGB값은 {dic[enter]}입니다')
else:
    print(f'{enter} 칼라의 RGB값을 찾을 수 없습니다')