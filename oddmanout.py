n = int(input())
for i in range(n):
    g = int(input())
    c = list(map(int, input().split()))
    
    alone = list(x for x in c if c.count(x)==1)
    print("case #{}: {}".format(i+1, alone[0]))