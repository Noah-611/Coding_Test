import sys
input = sys.stdin.readline

A=[]
N = int(input())

for i in range(N):
    command = input().split()
    if command[0] == 'push':
        A.append(command[1])
    elif command[0] == 'pop':
        if not A:
            print(-1)
        else:
            print(A.pop(0))
    elif command[0]=='size':
        print(len(A))
    elif command[0] == 'empty':
        if not A:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not A:
            print(-1)
        else:
            print(A[0])
    elif command[0] == 'back':
        if not A:
            print(-1)
        else:
            print(A[len(A)-1])
