def number_all_sum(*p):
    sum = 0
    for i in p:
        if type(i) ==int:
            sum += i
        else:
            pass
    if sum == 0:
        return
    else:
        return sum

print(number_all_sum(1,2,3,4,5))
print(number_all_sum(1,2,'a',3,4,'b',5))
print(number_all_sum(10,20,True))
print(number_all_sum())
print(number_all_sum('a',True,'가'))