import math
n = int(input())
for _ in range(n):
    s = input()
    k = math.ceil(math.sqrt(len(s)))
    # m = k**2
    
    m2 = [['*']*k for _ in range(k)]
    for inx, char in enumerate(s):
        row = inx // k
        col = inx % k
        m2[row][col] = char

    flip = zip(*m2[::-1])
    message = ''.join([''.join(x) for x in flip])
    print(message.replace('*', ''))