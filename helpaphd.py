n = int(input())
for _ in range(n):
    x = input()
    if '+' in x:
        a,b = map(int, x.split('+'))
        print(a+b)
    else:
        print('skipped')