N= int(input())

for i in range(N):
    S= input()
    cnt=0
    total=0
    for j in S:
        if j == 'O':
            cnt +=1
            total +=cnt
        else:
            cnt=0
    print(total)
