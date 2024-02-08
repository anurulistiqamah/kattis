symbol = {'.':20, 'O':10, '\\': 25, '/': 25, 'A':35, '^':5, 'v':22}
n, _ = map(int, input().split())
total = sum(symbol.get(x, 0) for _ in range(n) for x in input())
print(total)

# symbol = {'.':20, 'O':10, '\\': 25, '/': 25, 'A':35, '^':5, 'v':22}
# n, _ = map(int, input().split())
# total = 0
# for _ in range(n):
#     string = input()
#     for x in string:
#         if x in symbol.keys():
#             total += symbol[x]
# print(total)