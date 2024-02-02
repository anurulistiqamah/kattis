m = int(input())
n = int(input())

empty = 0
for _ in range(n):
    cars = input()
    empty += cars.count('.')

print(empty/(m*n))