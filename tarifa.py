x = int(input()) #megabytes
n = int(input()) #months
rest = 0
for i in range(n):
    pi = int(input()) #pi
    rest += x-pi
print(x+rest)