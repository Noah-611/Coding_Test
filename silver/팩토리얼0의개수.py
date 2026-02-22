def fact(n):
    if n <=1:
        return 1
    return n * fact(n-1)

N = int(input())
cnt = 0
result = str(fact(N))
for i in reversed(result):
    if i != '0':
        print(cnt)
        break
    elif i =='0':
        cnt +=1
