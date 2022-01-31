t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))[:-1]
    p = l[0]
    imp = 0
    for i in range(len(l)):
        if l[i] - 2*p > 0:
            imp += l[i] - 2*p
        p = l[i]
    
    print(imp)