n = int(input())
while n > 0:
    total = 0
    t0 = 0
    for i in range(n):
        s, t = map(int, input().split())
        total += s *(t-t0)
        t0 = t
    
    print(total, 'miles')
    n = int(input())