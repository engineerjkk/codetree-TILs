import sys
from collections import deque
n,m = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

dr=[1,0,-1,0]
dc=[0,-1,0,1]

def bfs(space,r,c):
    queue=deque()
    queue.append((r,c))
    cnt=1
    while queue:
        r,c=queue.popleft()
        space[r][c]=0
        for k in range(4):
            nr=r+dr[k]
            nc=c+dc[k]
            if -1<nr<n and -1<nc<m and space[nr][nc]>0:
                space[nr][nc]=0
                cnt+=1
                queue.append((nr,nc))
    return cnt


place=[[0]*m for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if space[i][j]>0:
            value=bfs(space,i,j)
            ans=max(ans,value)

if ans>0:
    print(ans)
else:
    print(-1)