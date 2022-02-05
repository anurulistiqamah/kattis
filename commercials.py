n, p = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    l[i] = l[i] - p

dp = []
dp.append(l[0])
for i in range(1,n):
    dp.append(max(l[i],dp[i-1]+l[i]))
    print(dp)
print(max(dp))