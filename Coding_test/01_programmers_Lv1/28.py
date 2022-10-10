# 부족한 금액 계산하기
def solution(price, money, count):
    answer = max(price*(count+1)*(count)//2 - money, 0)     

    return answer