import sys
input = sys.stdin.readline
from collections import deque

# 격자 크기 n, 사람 수 h, 비 피할 수 있는 공간 수 m
n, h, m = tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

ans=[[0]*n for _ in range(n)]
def bfs(a,b):
    visited=[[False]*n for _ in range(n)]
    #tmp=[[0]*n for _ in range(n)]
    queue=deque()
    queue.append((a,b,0))
    while queue:
        r,c,cnt=queue.popleft()
        if lst[r][c]==3:
            ans[a][b]=cnt
            return
        cnt+=1
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n and lst[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc]=True
                #tmp[nr][nc]=cnt
                queue.append((nr,nc,cnt))
    ans[a][b]=-1
    return

for i in range(n):
    for j in range(n):
        if lst[i][j]==2:
            bfs(i,j)

for i in range(n):
    for j in range(n):
        print(ans[i][j],end=" ")
    print()