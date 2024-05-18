import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

# 도시크기 n, 도시의 수, k 높이 u,d 사이
n,k,u,d=tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

space=[]
for i in range(n):
    for j in range(n):
        space.append([i,j])

nCr=combinations(space,k)

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def bfs(visited,r,c):
    queue=deque()
    queue.append((r,c))
    while queue:
        r,c=queue.popleft()
        visited[r][c]=2
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n and visited[nr][nc]==0:
                diff=abs(lst[r][c]-lst[nr][nc])
                if diff>=u and diff<=d :
                    visited[nr][nc]=2
                    queue.append((nr,nc))
    
ans=0
for x in nCr:
    cnt=0
    visited=[[0]*n for _ in range(n)]
    for i,j in x:
        visited[i][j]=1
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1:
                bfs(visited,i,j)
    for i in range(n):
        for j in range(n):
            if visited[i][j]==2:
                cnt+=1
    ans=max(ans,cnt)
print(ans)