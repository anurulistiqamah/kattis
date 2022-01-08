n = int(input())
for x in range(n):
    g = list(map(int, input().split()))
    first = g[1]
    for i in range(1, len(g)):
        if g[i] == first: first += 1
        else: print(i)