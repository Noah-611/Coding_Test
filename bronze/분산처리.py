T = int(input())
cnt =0
while cnt < T:
    a,b = map(int,input().split())
    num = pow(a,b,10)
    if num ==0:
        print(10)
    else:
        print(num)
    cnt +=1
