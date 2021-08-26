t = int(input())
for _ in range(t):
    n = int(input())
    place = set()
    for __ in range(n):
        place.add(input())

    print(len(place))