import sys
input = sys.stdin.readline
from itertools import combinations
n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

people=[]
hospital=[]
for i in range(n):
    for j in range(n):
        if space[i][j]==1:
            people.append((i,j))
        if space[i][j]==2:
            hospital.append((i,j))

def cal(x):
    total_dis=0
    for pr,pc in people:
        distance=sys.maxsize
        for hr, hc in x:
            distance=min(distance,abs(pr-hr)+abs(pc-hc))
        total_dis+=distance
    return total_dis

ans=sys.maxsize
nCr = combinations(hospital,m)
for x in nCr:
    ans=min(ans,cal(x))
print(ans)