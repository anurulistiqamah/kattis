abc_int = sorted(list(map(int, input().split())))
abc_string = input()

for i in abc_string:
    if i == "A":
        print(abc_int[0]),
    elif i == "B":
        print(abc_int[1]),
    else:
        print(abc_int[2])