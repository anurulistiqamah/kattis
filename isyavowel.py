string = input()

cv,y = 0,0
vowel = ['a', 'i', 'u', 'e', 'o']
for c in string:
    if c in vowel: cv += 1 #char vowel
    elif c == 'y': y += 1

print(cv,(cv+y))