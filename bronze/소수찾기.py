def prime_num(X):
    if X <2:
        return False
    for i in range(2, X):
        if X % i ==0:
            return False
    return True 


N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for i in numbers:
    if prime_num(i):
        cnt +=1
print(cnt)