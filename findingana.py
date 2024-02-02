string = input()

find_a, idx = 0, 0
for i in range(len(string)):
    if string[i] == 'a': 
        find_a = 1
        idx = i
        break

print(string[idx::])