import sys

def ordertest(A):
    return all(A[i] >= A[i+1] for i in range(len(A)-1))

while sys.stdin:
    n = int(input())
    inp = []
    out = []
    s, q, pq = 0,0,0 
    for _ in range(n):
        mode, element = map(int, input().split())
        if mode == 1: 
            inp.append(element)
        else:
            out.append(element)
        
    if inp == out: q = 1
    if inp == out[::-1]: s = 1
    if ordertest(out) and any(e in out for e in inp): pq = 1
    
    if s+q+pq>1: print("not sure")
    elif s > 0: print("stack")
    elif q > 0: print("queue")
    elif pq > 0: print("priority queue")
    else: print("impossible")


# I ALSO NOT SURE
# RUN TIME ERROR
# RUN TIME ERROR
# RUN TIME ERROR
# RUN TIME ERROR
# RUN TIME ERROR
# RUN TIME ERROR