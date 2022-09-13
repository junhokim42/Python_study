def in_python(str):
    if 'PYTHON' in str:
        return True
    else:
        return False

count = 0
while True:
    input_sentence = input("문자열을 입력하세요: ")
    while True:
        if in_python(input_sentence) == True:
            print('PYTHON이 존재합니다.')
        else:
            print('PYTHON이 존재하지 않습니다.')
        break
    count += 1
    if count > 2:
        break