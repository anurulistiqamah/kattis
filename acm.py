answer = []
mprw = input().split()
while int(mprw[0]) > -1:
    answer.append(mprw)
    mprw = input().split()

right = [x[1] for x in answer if x[2]=='right']
wrong = [x[1] for x in answer if x[1] in right and x[2]=='wrong']
rightsum = sum([int(x[0]) for x in answer if x[2]=='right']) + (len(wrong)*20)
print(len(right), rightsum)