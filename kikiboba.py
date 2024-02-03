string = input()

k = string.count('k')
b = string.count('b')

if k>b: print('kiki')
elif b>k: print('boba')
elif b==k and b>0: print('boki')
else: print('none')