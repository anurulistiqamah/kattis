def sum_of_digit(num):
    sod = 0
    for digit in str(num):
        sod += int(digit)
    return sod

n = int(input())
while n%sum_of_digit(n) != 0:
    n += 1
print(n) 