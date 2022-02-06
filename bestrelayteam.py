n = int(input())
d1 = []
d2 = []
for _ in range(n):
    name, a, b = input().split()
    d1.append((float(a), name))
    d2.append((float(b), name))

d1 = sorted(d1)[:4]
d2 = sorted(d2)[:4]
ans = []

for time, name in d1:
    names = [name]
    for i in range(len(d2)):
        if d2[i][1] != name and len(names) < 4:
            names.append(d2[i][1])
            time += d2[i][0]
    ans.append((time, names))

ans = sorted(ans)
print(ans[0][0])
for name in ans[0][1]:
    print(name)