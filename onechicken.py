n, m = map(int, input().split())
dif = abs(n-m)

if dif == 1: p = "piece"
else: p = "pieces"

if n > m:
    print("Dr. Chaz needs {0} more {1} of chicken!".format(dif,p))
else:
    print("Dr. Chaz will have {0} {1} of chicken left over!".format(dif,p))