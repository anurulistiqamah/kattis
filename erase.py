n = int(input())
bfd = input()
afd = input()

if n%2==1:
    check = bfd.replace('0','o').replace('1','0').replace('o','1')
else:
    check = bfd

print('Deletion succeeded' if check==afd else 'Deletion failed')