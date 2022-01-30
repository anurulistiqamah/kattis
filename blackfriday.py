from collections import Counter as count
n = input()
x = list(map(int, input().split()))
unique_value = [k for k,v in count(x).items() if v == 1]
print(x.index(max(unique_value))+1 if len(unique_value)>0 else "none")