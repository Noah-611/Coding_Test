import sys
input = sys.stdin.readline

N = int(input())
person=[]
for i in range(N):
    age, name = input().split()
    person.append((int(age), name))
person.sort(key = lambda x: x[0])

for age, name in person:
    print(age, name)