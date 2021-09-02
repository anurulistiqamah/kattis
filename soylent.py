t = int(input())
for _ in range(t):
    n = int(input())
    print(int(n/400) if n%400==0 else int(n/400)+1)