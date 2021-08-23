a = input().split(';')
l = 0
for x in a:
    if x.find('-') != -1:
        li = list(map(int, x.split('-')))
        l += li[1]-li[0]+1
    else:
        l += 1
print(l)