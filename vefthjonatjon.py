class veft:
    def __init__(self, value) -> None:
        self.range = value
        self.d = {}
    
    def count_j(self):
        for _ in range(self.range):
            nj = input().split()
            for k, v in enumerate(nj):
                if (v) == 'J':
                    self.d.setdefault(k, 0)
                    self.d[k] += 1
    
    def pair_j(self):
        print(min(self.d.values()))

veft = veft(int(input()))
veft.count_j()
veft.pair_j()

# n = int(input())
# d = {}
# for _ in range(n):
#     nj = input().split()
#     for k, v in enumerate(nj):
#         if (v) == 'J':
#             d.setdefault(k, 0)
#             d[k] += 1
        
# print(min(d.values()))