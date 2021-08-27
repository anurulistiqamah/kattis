cost = float(input())
lawns = int(input())
c = 0
for _ in range(lawns):
    l, w = map(float, input().split())
    c += l*w*cost
print("{:.6f}".format(c))