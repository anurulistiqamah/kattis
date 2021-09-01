cards = list(input().split())
pts = {}
for c in cards:
    if c[0] not in pts:
        pts[c[0]] = 1
    else:
        pts[c[0]] += 1
print(max(pts.values()))