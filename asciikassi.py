size = int(input())
len = size+2
for i in range(len):
    for j in range(len):
        # print(i,j,len)
        if (i==0 or i==len-1) and (j==0 or j==len-1):
            print("+", end="")
        elif (i==0 or i==len-1) and (j!=0 and j!=len-1):
            print("-", end="")
        elif (i!=0 and i!=len-1) and (j==0 or j==len-1):
            print("|", end="")
        else:
            print(" ", end="")
    print()