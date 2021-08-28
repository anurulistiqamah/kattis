sent = input().split()
print('yes' if len(sent) == len(set(sent)) else 'no')