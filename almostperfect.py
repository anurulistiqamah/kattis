from sys import stdin
for line in stdin:
    line = int(line)
    max = int(line**0.5) +1
    d = set()
    for i in range(1,max):
        if line%i == 0:
            d.add(i)
            d.add(line//i)

    d = sum(d)-line
    
    if line == d:
        p = 'perfect'
    elif abs(line-d) <= 2:
        p = 'almost perfect'
    else:
        p = 'not perfect'
    
    print(line, p)