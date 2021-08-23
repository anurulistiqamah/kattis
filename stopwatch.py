n = int(input())
running = False
total, prev = 0, 0
for i in range(n):
    t = int(input())
    if running:
        total += t - prev
    running = not running
    prev = t

if running:
    print('still running')
else:
    print(total)