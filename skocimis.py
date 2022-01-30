a, b, c = map(int, input().split())
move = 0
while c-b>1 or b-a>1:
    if b-a > c-b:
        b,c = b-1,b
        move += 1
    else:
        a,b = b,b+1
        move += 1
print(move)