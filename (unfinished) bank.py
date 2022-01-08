n, t = map(int, input().split())
cust = {}
for x in range(n):
    ci, ti = map(int, input().split())
    cust[ti] = cust.get(ti,[])+[ci]

serve = []
for i in range(t):
    if i in cust.keys():
        serve.append((max(cust.get(i)),i))
        cust[i].remove(max(cust.get(i)))
        cust = {k:v for k, v in cust.items() if v != []}
    print(cust)
print(sum(x[0] for x in serve))

# 4 4
# 1000 3
# 2000 3
# 500 3
# 1200 0