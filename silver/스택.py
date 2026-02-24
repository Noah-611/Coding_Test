import sys
input = sys.stdin.readline

N = int(input())
A = []
14
for i in range(N):
    command = input().split()

    if command[0] == 'push':
        A.append(command[1])

    elif command[0] == 'pop':
        if not A:
            print(-1)
        else:
            print(A.pop())

    elif command[0] == 'size':
        print(len(A))

    elif command[0] == 'empty':
        if not A:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if not A:
            print(-1)
        else:
            print(A[-1])