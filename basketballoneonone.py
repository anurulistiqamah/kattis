s = input()
point_a, point_b = 0, 0
for i,c in enumerate(s):
    if i%2==0 and c=='A':
        point_a += int(s[i+1])
    elif i%2==0 and c=='B':
        point_b += int(s[i+1])

print('A' if point_a>point_b else 'B')