c = int(input())
for _ in range(c):
    a = list(map(int, input().split()))
    del a[0]
    avg = sum(a)/len(a)
    abvavg = [x for x in a if x > avg]
    percent = len(abvavg)/len(a)*100
    print(format(percent,'.3f')+'%')