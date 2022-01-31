alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
s = input()
while s != '0':
    n, s = s.split()
    inx = []
    for x in s:
        inx.append(alphabet.index(x) + int(n))

    ans = []
    for y in inx:
        ans.append(alphabet[y%28])

    ans = ans[::-1]
    print(''.join(ans))
    
    s = input()