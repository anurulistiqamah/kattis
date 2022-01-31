n = int(input())
for _ in range(n):
    t = input()
    print(t[11:] if "simon says" in t[:10] else "")