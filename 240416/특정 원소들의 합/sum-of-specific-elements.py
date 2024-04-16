import sys
input = sys.stdin.readline

space=[]
for _ in range(4):
    space.append(list(map(int,input().split())))
SUM=0
for i in range(4):
    for j in range(4):
        if i==j or i>j:
            SUM+=space[i][j]

print(SUM)