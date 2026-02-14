searchStr = 'aeiouAEIOU'
while 1:
    s = str(input())
    cnt =0
    if s == '#':
        break
    else:
        for i in s:
            if i in searchStr:
                cnt +=1
    print(cnt)