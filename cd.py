from sys import stdin as s
n, m = map(int, s.readline().split())
while n + m != 0:
    jack = set()
    for _ in range(n):
        jack.add(int(s.readline()))

    common = 0
    for _ in range(m):
        if int(s.readline()) in jack:
            common += 1

    print(common)
    n, m = map(int, s.readline().split())