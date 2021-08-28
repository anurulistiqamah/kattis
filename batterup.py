n = int(input())
a = list(map(int, input().split()))
a = list(filter(lambda x: x!= -1, a))
print(sum(a)/len(a))