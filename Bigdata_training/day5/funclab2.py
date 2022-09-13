def get_book_title():
    book_title = input("파이썬 교재명 입력 : ")
    return book_title

def get_book_publisher():
    book_publisher = input("파이썬 교재 출판사명 입력 : ")
    return book_publisher

name = get_book_title()
print(name * 2)
print(get_book_publisher())