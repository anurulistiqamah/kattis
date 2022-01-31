m = int(input())
ans = input()

adrian = 'ABC'*m
bruno = 'BABCBABC'*m
goran = 'CCAABB'*m
a,b,g = 0,0,0

for i, e in enumerate(ans):
    if adrian[i] == e: a+=1
    if bruno[i] ==  e: b+=1
    if goran[i] ==  e: g+=1

maxvalue = max([a,b,g])
print(maxvalue)
if maxvalue == a: print("Adrian")
if maxvalue == b: print("Bruno")
if maxvalue == g: print("Goran")