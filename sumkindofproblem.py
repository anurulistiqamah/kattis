p = int(input())
for _ in range(p):
    k, n = map(int, input().split())
    s1 = n*(n+1)/2
    s2 = n**2
    s3 = n*(n+1)
    print(k, int(s1), s2, s3)