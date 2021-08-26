a = []
for i in range(5):
    pets = sum(list(map(int, input().split())))
    a.append(pets)

print(a.index(max(a))+1, max(a))