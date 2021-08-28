x = {'A':[11,11], 'K':[4,4], 'Q':[3,3], 'J':[20,2], 'T':[10,10], '9':[14,0], '8':[0,0], '7':[0,0]}
n,b = input().split()
point = 0
for _ in range(int(n)*4):
    card = input()
    if card[1] == b:
        point += x[card[0]][0]
    else:
        point += x[card[0]][1]
print(point)