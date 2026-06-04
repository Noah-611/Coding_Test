import sys, math
input = sys.stdin.readline

def prime_Num(X):
    arr = [True for i in range(X+1)]
    if X <2:
        return False
    for i in range(2, math.sqrt(X+1)):
        if arr[i]:
            for j in range(i*i, n+1, i):

        if X % i ==0:
            return False
    return True

M, N = map(int,input().split())

for i in range(M,N+1):
    if prime_Num(i):
        print(i)