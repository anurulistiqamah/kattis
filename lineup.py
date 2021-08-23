n = int(input())
names = []
for _ in range(n):
    x = input()
    if x not in names:
        names.append(x)

if names == sorted(names): print('INCREASING')
elif names == sorted(names, reverse=True): print('DECREASING')
else: print('NEITHER')