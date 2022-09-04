# enumerate

FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']
for idx, symbol in enumerate(FAANG, 1):
    print(idx, symbol)

print('\n')

# while else, for else

i = -1
while i >= 0:
    i += 1
    if (i%2) == 0:
        continue
    if i > 5:
        break
    print(i)
else:
    print('Condition is False\n')

# try except
try:
    1/0
except Exception as e:
    print('Exception occured :', str(e), '\n')

# split, join
myList = 'Thoughts become things.'.split()
type(myList)
print(myList)
' '.join(myList)