n, k, r = map(int, input().split()) # length martian dna, alphabet, nucleobases
di = list(map(int, input().split())) # di < k, len(di) == n
listbq = []
for _ in range(r):
    b, q = map(int, input().split()) # b < k, q <= n
    listbq.append([b,q])

print("di", di)
print("listbq", listbq)

listunique = []
listans = []
for i in range(len(di)):
    if i+1 != len(di):
        if di[i] != di[i+1]:
            listunique.append(di[i])
        else:
            listunique.append(di[i+1])
            listans.append(listunique)
            listunique = []

# print(listans)

for i in listans:
    for j in listbq:
        if set(j).issubset(i):
            answer = len(i)
        else:
            answer = 'impossible'

print(answer)