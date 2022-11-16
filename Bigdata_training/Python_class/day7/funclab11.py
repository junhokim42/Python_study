def sum_even(*p):
    sum = 0
    if p == ():
        return -1
    for i in p:
        if i % 2 == 0:
            sum += i
        else:
            pass
    return sum

print(sum_even(1,2,3,4,5))
print(sum_even(11,22,33,44,55))
print(sum_even(1,3,5))
print(sum_even())
