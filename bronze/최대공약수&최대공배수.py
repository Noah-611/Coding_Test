x,y = map(int, input().split())
i=1
gcd =1
while i<=min(x,y):
    if x%i ==0 and y%i ==0:
        gcd = i
    i+=1
lcm = x*y//gcd
print(gcd)
print(lcm)