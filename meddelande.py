n,m = map(int, input().split())
string = ''
for _ in range(n):
    path = input()
    for char in path:
        if char != '.':
            string += char

print(string)
