import sys
input = sys.stdin.readline
N = int(input())
A = []
for i in range(N):
    x,y = map(int, input().split())
    A.append((x,y))
A.sort()
print('\n'.join(f"{x} {y}" for x,y in A))