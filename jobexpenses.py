k = int(input())
exin = list(map(int, input().split()))
expenses = abs(sum([x for x in exin if x < 0]))
print(expenses)