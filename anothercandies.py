t = int(input())
for _ in range(t):
    input()

    n = int(input())
    candies = 0
    for x in range(n):
        candies += int(input())

    print("YES" if candies%n==0 else "NO")