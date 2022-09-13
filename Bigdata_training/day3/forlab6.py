even_num = 0
odd_num = 0
for i in range(1, 101):
    if i%2 == 0:
        even_num += i
    else:
        odd_num += i

print('1부터 100까지 숫자 중\n짝수의 합은 {}이고\n홀수의 합은 {}이다'.format(even_num, odd_num))