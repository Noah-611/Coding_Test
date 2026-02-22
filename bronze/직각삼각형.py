while True:
    x,y,z = map(int, input().split())

    a, b, R= sorted([x,y,z])
    if x==0 and y==0 and z==0:
        break
    if R*R == a*a + b*b:
        print('right')
    else:
        print('wrong')
