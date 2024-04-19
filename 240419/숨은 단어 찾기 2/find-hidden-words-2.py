import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

space=[]
for _ in range(n):
    space.append(list(map(str,input().strip())))

dr=[-1,-1,0,1,1,1,0,-1]
dc=[0,1,1,1,0,-1,-1,-1]

def bfs(space,r,c):
    tmp=0
    for d in range(8):
        nr=r+dr[d]
        nc=c+dc[d]
        nr2=nr+dr[d]
        nc2=nc+dc[d]
        if -1<nr<n and -1<nc<m and -1<nr2<n and -1<nc2<m and space[nr][nc]=="E" and space[nr2][nc2]=="E":
            tmp+=1
    return tmp

cnt=0
for i in range(n):
    for j in range(m):
        if space[i][j]=="L":
           cnt+=bfs(space,i,j)
print(cnt)