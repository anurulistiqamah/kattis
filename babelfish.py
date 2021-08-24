from sys import stdin

d = {}
for line in stdin:
    s = line.strip()
    if ' ' in s:
        word, fl = s.split()
        d[fl] = word
    elif s != '':
        print(d[s] if s in d.keys() else 'eh')  