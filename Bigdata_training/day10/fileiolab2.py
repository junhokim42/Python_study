try:
    with open("yesterday.txt", "rt", encoding="UTF-8") as f:
        count = 0
        for line in f.readlines():
            a = line.lower().count('yesterday')
            count += a  

except FileNotFoundError:
    print('파일을 읽을 수 없어요')

else:
    print(f'Number of a Word "Yesterday" {count}')
    
finally:
    print('수행완료!')