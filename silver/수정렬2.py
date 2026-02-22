import sys
input = sys.stdin.readline
n = int(input())
Q = list()
for i in range(n):
    a = int(input())
    Q.append(a)
Q.sort()
print('\n'.join(map(str,Q)))