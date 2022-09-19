while(True):
    try:
        a = int(input('숫자를 입력하세요: '))
        result = a*(a+1)//2
        print(f'1부터 {a}까지의 합은' + ' %d입니다'%result)
        break
    except ValueError:
        print('숫자만 입력해 주세요~~')