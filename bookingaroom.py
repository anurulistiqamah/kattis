r, n = map(int, input().split())
booked = []
for _ in range(n):
    booked.append(int(input()))

notbooked = [x for x in range(1,100) if x not in booked]
print('too late' if r==n else notbooked[0])