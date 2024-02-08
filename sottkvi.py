class sott:
    def __init__(self):
        self.n, self.k, self.d = map(int, input().split())
        self.total = 0

    def total_friend(self):
        for _ in range(self.n):
            qrntn_of_friend = int(input())
            if (self.k + self.d) - qrntn_of_friend >= 14:
                self.total += 1

        print(self.total)

sott = sott()
total = sott.total_friend()

# simple version
# n, k, d = map(int, input().split())
# total = 0
# for _ in range(n):
#     if k+d - int(input()) >= 14:
#         total += 1
# print(total)