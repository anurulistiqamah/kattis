n = int(input())
arr = []
for _ in range(n):
    command, num = input().split()
    if command == 'push_back':
        arr.insert(len(arr), num)
    elif command == 'push_front':
        arr.insert(0, num)
    elif command == 'push_middle':
        inx = int((len(arr)+1)/2)
        arr.insert(inx, num)
    else:
        print(arr[int(num)])

# TIME LIMIT EXCEEDED
# TIME LIMIT EXCEEDED
# TIME LIMIT EXCEEDED
# TIME LIMIT EXCEEDED
# TIME LIMIT EXCEEDED