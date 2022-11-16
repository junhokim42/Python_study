listv = ['p', 'y', 't', 'h', 'o', 'n']
v1, v2, v3, v4, v5, v6 = listv

for i in range(len(listv)):
    eval(f"print(v{i+1})")

for i in range(len(listv)):
    print(listv[i], end=' ')
print()
print(listv)
print(*listv)