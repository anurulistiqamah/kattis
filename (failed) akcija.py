n = int(input())
cost = []
for _ in range(n):
    cost.append(int(input()))

cost = sorted(cost,reverse=True)
pay = n//3
print(sum(cost[:pay*2])+sum(cost[pay*2+pay:]))