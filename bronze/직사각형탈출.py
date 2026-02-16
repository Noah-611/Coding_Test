x, y, w, h = map(int,input().split())

if x<(w/2) and y<(h/2):
    if x>y:
        print(y)
    else:
        print(x)
else:
    if (w-x)>(h-y):
        print(h-y)
    else:
        print(w-x)