import sys
input = sys.stdin.readline
from collections import deque

n,k=tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

final=[[0]*n for _ in range(n)]
check=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][j]!=1:
            check[i][j]=True
def bfs(a,b):
    visited=[[0]*n for _ in range(n)]

    queue=deque()
    cnt=0
    queue.append((a,b,cnt))
    while queue:
        r,c,cnt=queue.popleft()
        cnt+=1
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n and visited[nr][nc]==0 and lst[nr][nc]==1:
                visited[nr][nc]=cnt
                #final[nr][nc]=cnt
                if final[nr][nc]==0:
                    final[nr][nc]=cnt
                elif final[nr][nc]>cnt:
                    final[nr][nc]=cnt
                check[nr][nc]=True
                queue.append((nr,nc,cnt))

for i in range(n):
    for j in range(n):
        if lst[i][j]==2:
            bfs(i,j)

for i in range(n):
    for j in range(n):
        if lst[i][j]==2:
            final[i][j]=0

for i in range(n):
    for j in range(n):
        if check[i][j]==False:
            final[i][j]=-2

for i in range(n):
    for j in range(n):
        if lst[i][j]==0:
            final[i][j]=-1

for i in range(n):
    for j in range(n):
        print(final[i][j],end=" ")
    print()