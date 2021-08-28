n = int(input())
for _ in range(n):
    fs = input()
    ss = input()
    out = ''
    for i in range(len(fs)):
        if fs[i]==ss[i]: out += '.'
        else: out += '*'
    print(fs+'\n'+ss+'\n'+out, end='\n\n')