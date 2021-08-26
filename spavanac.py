h, m = map(int, input().split())
total = ((h*60)+m)-45
if total//60 > 0:
    print(total//60, total%60)
else:
    print(total//60+24, total%60)