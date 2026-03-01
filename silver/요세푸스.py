import sys
input = sys.stdin.readline

N, K = map(int,input().split())
A = lis(range(1,N+1))
B =[]
idx=0
while A:
    for _ in range(K - 1):
        A.append(A.pop(0))
    B.append(A.pop(0))
print("<"+",".join(map(str,B))+">")