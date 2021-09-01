n = int(input())
a = {}
for _ in range(n):
    c, r = input().split()
    if not r.isdigit():
        c = int(c)/2
        c, r = r, c
    r = int(r)
    a[c] = r

a = sorted(a.items(), key=lambda item: item[1])
for i in a:
    print(i[0])