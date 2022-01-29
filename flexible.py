w, p = map(int, input().split())
collider = [0]+list(map(int, input().split()))+[w]
arr = []

for i in range(len(collider)):
    for j in range(i+1, len(collider)):
        arr.append(collider[j]-collider[i])

print(*sorted(set(arr)))