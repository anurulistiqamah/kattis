n = int(input())
m = []
for _ in range(n):
    m.append(int(input()))

if len(m) == m[-1]: print('good job')
for i in range(1, m[-1]):
    if i not in m:
        print(i)