n = int(input())
lose = 0
for _ in range(n):
    s = input()
    p = s[0]
    for x in s[1:]:
        if p == 'C' and x == 'D':
            lose += 1
            continue
        p = x
print(n-lose)