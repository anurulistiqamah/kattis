n = int(input())
num = []
for i in range(n):
    num.append(input())
rev = num[::-1]
print("\n".join(rev))