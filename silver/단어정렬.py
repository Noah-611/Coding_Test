import sys
input=sys.stdin.readline

N = int(input())
A=[]
for i in range(N):
    A.append(input().strip())
A=list(set(A))
A.sort()
A.sort(key=len)
print('\n'.join(A))
