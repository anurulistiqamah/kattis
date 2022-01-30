a, b = 1,0
k = int(input())
for _ in range(k):
    a, b = b, b+a
print(a, b)