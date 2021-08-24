n = int(input())
while n > 0:
    names = []
    for _ in range(n):
        names.append(input())

    sort = sorted(names, key=lambda x:x[:2])
    print(*sort, sep='\n')

    print()
    n = int(input())