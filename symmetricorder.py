n = int(input())
s = 1
while n > 0:
    names = []
    print('SET', s)
    for i in range(n):
        if (i%2==0):
            print(input())
        else:
            names.append(input())

    for n in reversed(names):
        print(n)

    s += 1
    n = int(input())