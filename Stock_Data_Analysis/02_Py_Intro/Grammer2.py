import timeit

# Dictionary

crispr = {'EDIT': 'Editas Medicine', 'NTLA': 'Intellia Therapeutics'}

for x in crispr:
    print('%s : %s' % (x, crispr[x]))

# Timeit

search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr:
    pass
"""

print(timeit.timeit(search_test, setup = 'itr = list(range(100))', number = 1000))

# CAGR

def getCAGR(first, last, years):
    return (last/first)**(1/years) - 1

cagr = getCAGR(65300, 2669000, 20)
print('SEC CAGR : {:.2%}'.format(cagr))