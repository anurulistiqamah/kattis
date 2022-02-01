from sys import stdin
d = {}
for line in stdin:
    s = line.strip().split()
    if s[0] == 'clear':
        d = {}
    elif s[0] == 'def':
        d[s[1]] = int(s[2])
    elif s[0] == 'calc':
        total = 0
        known = True

        # first var to calculate
        if s[1] in d.keys():
            total += d[s[1]]
        else: known = False

        # second var until end to calculate 
        for i in range(3, len(s), 2):
            if s[i] in d.keys() and s[i-1] == '+':
                total += d[s[i]]
            elif s[i] in d.keys() and s[i-1] == '-':
                total -= d[s[i]]
            else: known = False
        
        if known and total in d.values():
            print(*s[1:], list(d.keys())[list(d.values()).index(total)])
        else:
            print(*s[1:], 'unknown')