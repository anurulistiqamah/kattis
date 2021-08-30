gunnar = sum(list(map(int, input().split())))
emma = sum(list(map(int, input().split())))
if gunnar > emma:
    print('Gunnar')
elif gunnar < emma:
    print('Emma')
else:
    print('Tie')