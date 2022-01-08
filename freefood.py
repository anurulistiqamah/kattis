n = int(input())
arr = {}
for x in range(n):
    t,s = map(int, input().split())
    for i in range(t-1,s):
        arr[i] = 1
print(len(arr))