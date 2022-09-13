word = input('문자열을 입력하세요 : ')
wordlength = len(word)
result = ''
while wordlength != 0:
    if 5 <= wordlength <= 8:
        word = input('문자열을 입력하세요 : ')
        wordlength = len(word)
        continue
    elif wordlength < 5:
        result = '*' + word + '*'
        break
    else:
        result = '$' + word + '$'
        break
print(result)
