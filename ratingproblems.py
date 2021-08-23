n, k = map(int, input().split())
sr = 0
for _ in range(k):
    sr += int(input())
print((sr+(n-k)*(-3))/n, (sr+(n-k)*(3))/n)