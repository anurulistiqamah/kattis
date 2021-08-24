import sys
for linenum, line in enumerate(sys.stdin):
    x = list(map(int, line.split()))
    del x[0]
    print('Case {3}: {0} {1} {2}'.format(min(x), max(x), max(x)-min(x), linenum+1))