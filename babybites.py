n = int(input())
l = list(input().split())
makesense = True

for i,x in enumerate(l):
    if x != 'mumble' and x != str(i+1):
        makesense = False

if makesense: print('makes sense')
else: print('something is fishy')