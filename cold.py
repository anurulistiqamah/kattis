n = int(input())
t = list(map(int, input().split()))
lz = []
for i in t:
    if i < 0:
        lz.append(i)
print(len(lz))