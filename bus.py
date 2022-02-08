t = int(input())
for _ in range(t):
    k = int(input())
    initial = 1
    for i in range(k):
        initial += (initial/2) + (initial/2)
    
    print(int(initial)-1)