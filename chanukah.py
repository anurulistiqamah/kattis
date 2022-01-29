p = int(input())
for i in range(p):
    k, n = map(int, input().split())
    sum = n/2*(n+3) #formula: n/2 x (a+n) for a = 1+1; n = n+1
    print(k, int(sum))