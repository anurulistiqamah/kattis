n, h, v = map(int, input().split())
hr = n-h
vr = n-v
print(max(h,hr)*max(v,vr)*4)