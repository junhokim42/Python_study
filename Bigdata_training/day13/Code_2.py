if __name__ == "__main__":
    while (select != 4):
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료) => "))

        if (select == 1):
            data = input("추가할 데이터 -> ")
            add_data(data)
            print(katok)
        elif (select == 2):
            pos = int(input("삽입할 위치 -> "))
            data = input("추가할 데이터 -> ")
            insert_data(pos, data)
            print(katok)
        elif (select == 3):
            pos = int(input("삭제할 위치 -> "))
            delete_data(pos)
            print(katok)
        elif (select == 4):
            print(katok)
            exit
        else:
            print("1~4 중 하나를 입력하세요")
            continue
