name = input()
n, p = '', ''
for i in name:
    if p != i:
        n += i
        p = i
print(n)