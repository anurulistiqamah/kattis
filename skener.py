r,c,zr,zc = map(int, input().split())
for _ in range(r):
    mt = input()
    str = ''
    for x in mt:
        str += x*zc

    for y in range(zr):
        print(str)