n = int(input())
total = 0
for _ in range(n):
    pi = int(input())
    number = pi//10
    power = pi%10
    total += pow(number, power)
print(total)