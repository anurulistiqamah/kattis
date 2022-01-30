n = int(input())
for _ in range(n):
    pstrip = list(map(int, input().split()))[1:]
    print(sum(pstrip)-(len(pstrip)-1))