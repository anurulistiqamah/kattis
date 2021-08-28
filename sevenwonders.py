s = input()
t,g,c = 0,0,0
for i in s:
    if(i=='T'): t+=1
    elif(i=='C'): c+=1
    else: g+=1
print(t**2+c**2+g**2+min(t,c,g)*7)    