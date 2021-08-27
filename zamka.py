l = int(input())
d = int(input())
x = int(input())
a = []

for i in range(l,d+1):
    sod = 0 #sum of digits
    for digit in str(i):
        sod += int(digit)
    if sod == x:
        a.append(i)

print(min(a))
print(max(a))