n = int(input())
for _ in range(n):
    s = input()
    k = int(len(s)**0.5)
    
    m2 = [['*']*k for _ in range(k)]
    for inx, char in enumerate(s):
        row = inx // k
        col = inx % k
        m2[col][row] = char

    print(''.join([''.join(x) for x in m2[::-1]]))