arr = []
for _ in range(10):
    num = int(input())
    modulo = num%42
    if modulo not in arr:
        arr.append(modulo)

print(len(arr))