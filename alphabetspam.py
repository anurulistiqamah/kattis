string = input()
ws,lc,uc,sy=0,0,0,0
for c in string:
    if c == '_': ws+=1
    elif c.islower(): lc+=1
    elif c.isupper(): uc+=1
    else: sy+=1
print(ws/len(string)) #whitespace
print(lc/len(string)) #lowecase
print(uc/len(string)) #uppercase
print(sy/len(string)) #symbol