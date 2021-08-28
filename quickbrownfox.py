n = int(input())
az = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(n):
    out = ''
    sent = input().lower()
    for x in az:
        if x not in sent:
            out += x

    if len(out) == 0:
        print('pangram')
    else:
        print('missing', out)