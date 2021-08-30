e, f, c = map(int, input().split())
emptysodas = e+f
newsodas = 0

while emptysodas >= c:
    emptysodas -= (c-1)
    newsodas += 1
print(newsodas)