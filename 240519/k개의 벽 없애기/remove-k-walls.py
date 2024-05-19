import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy 

n,k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

r1,c1 =tuple(map(int,input().split()))
r2,c2 = tuple(map(int,input().split()))
r1-=1
c1-=1
r2-=1
c2-=1

wall=[]
for i in range(n):
    for j in range(n):
        if lst[i][j]==1:
            wall.append((i,j))

nCr = combinations(wall,k)


dr=[-1,0,1,0]
dc=[0,1,0,-1]
check=False
ans=sys.maxsize
for x in nCr:
    cnt=0
    queue=deque()
    queue.append((r1,c1,cnt))
    visited=[[0]*n for _ in range(n)]
    visited[r1][c1]='*'
    tmp=copy.deepcopy(lst)
    for a,b in x:
        tmp[a][b]=0
    while queue:
        r,c,cnt=queue.popleft()
        cnt+=1
        if r==r2 and c==c2:
            ans=min(ans,visited[r][c])
            check=True
            break
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n and tmp[nr][nc]==0 and visited[nr][nc]==0:
                visited[nr][nc]=cnt
                queue.append((nr,nc,cnt))
if check:
    print(ans)
else:
    print(-1)