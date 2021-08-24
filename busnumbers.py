from itertools import groupby, count

n = int(input())
b = sorted(list(map(int, input().split())))

def as_range(iterable):
    l = list(iterable)
    if len(l) > 2:
        return '{0}-{1}'.format(l[0], l[-1])
    elif len(l) == 2:
        return '{0} {1}'.format(l[0], l[-1])
    else:
        return '{0}'.format(l[0])

b = ' '.join(as_range(g) for _, g in groupby(b, key=lambda n, c=count(): n-next(c)))
print(b)