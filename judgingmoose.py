r, l = map(int, input().split())
if r+l>0:
    print('Odd' if r!=l else 'Even', max(r,l)*2)
else:
    print('Not a moose')