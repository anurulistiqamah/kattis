inx = []
for i in range(5):
    if "FBI" in input():
        inx.append(i+1)

print(*inx) if len(inx)>0 else print('HE GOT AWAY!')