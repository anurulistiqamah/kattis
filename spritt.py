n,x = map(int, input().split())

a = 0
for _ in range(n):
    a += int(input())

if x >= a: print('Jebb')
else: print('Neibb')