p, n = map(int, input().split())
boatparts = []
day = 0
for i in range(n):
    w = input()
    if w not in boatparts:
        boatparts.append(w)
        day = i+1

if len(boatparts) == p:
    print(day)
else:
    print('paradox avoided')