sent = input()
ans = []

for x in sent:
    if x != '<':
        ans.append(x)
    else:
        ans.pop()

print(''.join(ans))