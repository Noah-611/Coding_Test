import sys
input = sys.stdin.readline

N = int(input())
ori_N = N
cnt = 0
while True:
    a = N//10
    b = N%10
    N = b*10+(a+b)%10
    cnt +=1
    if ori_N == b*10+(a+b)%10:
        break
print(cnt)
