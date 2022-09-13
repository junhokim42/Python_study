print([x for x in range(10)])
print([x*x for x in range(10)])
print([x for x in range(10) if x%2 == 0])
print([x for x in range(10) if x%2 == 1])
print([x*x for x in range(10) if x%2 == 0])
print([x*x for x in range(10) if x%2 == 1])

s = input('정수 5개를 입력하세요: ').split()
print(s)

product_xy = []

for x in (1, 2, 3):
    for y in (2, 4, 6):
        product_xy.append(x*y)

print(product_xy)

result = [i if i%2 == 0 else 10 for i in range(10)]
print(result)