from sys import stdin
words = []
for i in stdin:
    words = words + i.split()

result = sorted(set([i+j for i in words for j in words if i!=j]))
print('\n'.join(result))