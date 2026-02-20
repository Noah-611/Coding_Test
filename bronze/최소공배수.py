import sys
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
N = int(input())
for i in range(N):
    x,y = map(int,input().split())
    g = gcd(x,y)
    print(x*y//g)