n = int(input())
l = []
for _ in range(n):
    mode, name = input().split()
    if mode == 'entry':
        if name not in l:
            l.append(name)
            print(name, 'entered')
        else:
            print(name, 'entered (ANOMALY)')
    else:
        if name in l:
            l.remove(name)
            print(name, 'exited')
        else:
            print(name, 'exited (ANOMALY)')