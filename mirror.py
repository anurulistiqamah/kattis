n = int(input())
for i in range(n):
    rows, columns = map(int, input().split())
    char = []
    for row in range(rows):
        string = input()[::-1]
        char.append(string)

    print(f"Test {i+1}")
    print("\n".join(char[::-1]))