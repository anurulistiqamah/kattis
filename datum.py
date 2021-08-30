from datetime import date
d, m = map(int, input().split())
y = 2009
print(date(y,m,d).strftime('%A'))