n, time = map(int, input().split())
task = list(map(int, input().split()))
cmpltd = []
for i in range(n):
    time -= task[i]
    if time >= 0:
        cmpltd.append(task[i])

print(len(cmpltd))