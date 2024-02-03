n = int(input())
array = list(map(int, input().split()))

prob = 0
for x in array: # x is placed hotel
    for y in range(x): # y is distance to x (could be 1st dice)
        z = x-y # 2nd dice
        if z >= 1 and z <= 6 and y >= 1 and y <= 6 and z+y==x:
            # print(z,y)
            prob += 1

print(prob/36)