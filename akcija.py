n = int(input())
cost = []
for _ in range(n):
    cost.append(int(input()))

cost = sorted(cost,reverse=True)
pay = sum([cost[x] for x in range(len(cost)) if x%3 != 2])
print(pay)