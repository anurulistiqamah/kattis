char = input()
ball = [1,0,0]

for i in range(len(char)):
    if char[i] == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif char[i] == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[0], ball[2] = ball[2], ball[0]

print(ball.index(1)+1)