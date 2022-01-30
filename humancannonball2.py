import math
n = int(input())
for _ in range (n):
    v, th, x, h1, h2 = map(float, input().split())
    th = math.radians(th)
    t = x/(v*math.cos(th))
    y = (v*t*math.sin(th))-(4.905*(t**2))
    print("Safe" if h1+1 <= y and y <= h2-1 else "Not Safe")