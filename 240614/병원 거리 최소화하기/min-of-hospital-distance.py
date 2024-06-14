import sys
input = sys.stdin.readline
from itertools import combinations
n,m = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

lst=[]
people=[]
for i in range(n):
    for j in range(n):
        if space[i][j]==2:
            lst.append((i,j))
        if space[i][j]==1:
            people.append((i,j))
nCr=combinations(lst,m)
final_total_distance=sys.maxsize

def cal(x):
    score=0
    for pr,pc in people:
        distance=sys.maxsize
        for hr,hc in x:
            distance=min(distance,abs(pr-hr)+abs(pc-hc))
        score+=distance
    return score
answer=sys.maxsize
for x in nCr:
    answer=min(answer,cal(x))
print(answer)