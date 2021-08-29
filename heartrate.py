n = int(input())
for _ in range(n):
    b, p = map(float, input().split())
    bpm = (60*b)/p
    abpm = 60/p
    print(bpm-abpm, bpm, bpm+abpm)