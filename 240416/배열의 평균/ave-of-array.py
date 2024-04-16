import sys
input=sys.stdin.readline
space=[]
for i in range(2):
    space.append(list(map(float,input().split())))


for i in (space):
    print(round(sum(i)/len(i),1),end=" ")
print()
for j in range(4):
    a=[]
    for i in range(2):
        a.append(space[i][j])
    b=sum(a)/len(a)
    print(round(b,1),end=" ")
print()

total=[]
for i in range(2):
    for j in range(4):
        total.append(space[i][j])
print(round((sum(total)/len(total)),1))