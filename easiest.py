def sod(num):
    sod = 0
    for i in str(num):
        sod += int(i)
    return sod

n = int(input())
while n > 0:
    p = 11 
    sodn = sod(n)
    sodx = sod(n * p)

    while sodx != sodn:
        p += 1
        sodx = sod(n * p)

    print(p)
    n = int(input())