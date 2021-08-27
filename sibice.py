from math import hypot
n, w, h = map(int, input().split())
pythagoras = hypot(w,h)
for _ in range(n):
    m = int(input())
    print('DA' if m <= pythagoras else 'NE')