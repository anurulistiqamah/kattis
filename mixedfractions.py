n, d = map(int, input().split())
while n+d > 0:
    print(n//d, n%d, '/', d)
    n, d = map(int, input().split())