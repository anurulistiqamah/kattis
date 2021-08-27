n = int(input())
for _ in range(n):
    says = input()
    if "Simon says" in says:
        print(says.replace('Simon says',''))