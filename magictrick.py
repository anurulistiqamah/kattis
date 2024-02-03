data = lambda x: len(x) == len(set(x))
print(1 if data(input()) else 0)