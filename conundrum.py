text = input().lower()
days = 0
for i in range(len(text)):
    if i%3==0 and text[i]!='p': days+=1
    elif i%3==1 and text[i]!='e': days+=1
    elif i%3==2 and text[i]!='r': days+=1
print(days)