from math import sin, radians
h, v = map(int, input().split()) #h is height, v is degree
print(int(-(-h//sin(radians(v)))))