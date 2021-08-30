sent = input()
ans = []
x = 0
while x < len(sent):
    ans.append(sent[x])
    if sent[x] in 'aiueo':
        x+=3
    else:
        x+=1
print(''.join(ans))