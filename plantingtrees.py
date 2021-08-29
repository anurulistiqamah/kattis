n = int(input()) # number of trees
a = sorted(list(map(int,input().split())), reverse=True)
for i in range(n):
    a[i] += i+1
print(max(a)+1)