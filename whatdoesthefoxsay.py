t = int(input())
for _ in range(t):
    s = input().split()
    says = s
    while s[0] != "what":
        s = input().split()
        if s[1] == "goes":
            says = list(filter(lambda a: a!=s[2], says))
    print(*says)