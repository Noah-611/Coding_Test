N=int(input())

A=list(map(int, input().split()))
M= max(A)
for i in range(N):
    A[i]=A[i]/M * 100
total = 0
for i in range(N):
    total +=A[i]
mean=total/N
print(mean)