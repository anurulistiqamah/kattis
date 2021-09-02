l, x = map(int, input().split())
limit = l
reject = 0
for _ in range(x):
    xi = input().split()
    if 'enter' in xi[0]:
        if l-int(xi[1]) >= 0:
            l -= int(xi[1])
        else:
            reject += 1
    else:
        if l < limit:
            l += int(xi[1]) 
print(reject)