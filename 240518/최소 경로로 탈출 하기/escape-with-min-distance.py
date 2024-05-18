import sys
input = sys.stdin.readline
from collections import deque

n,m = tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

queue=deque()
queue.append((0,0,0))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

visited=[['*']*m for _ in range(n)]
visited[0][0]=0

cnt=0
while queue:
    r,c,cnt = queue.popleft()
    cnt+=1
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if -1<nr<n and -1<nc<m and lst[nr][nc]==1 and visited[nr][nc]=='*':
            visited[nr][nc]=cnt
            queue.append((nr,nc,cnt))

# for i in range(n):
#     print(visited[i])

if visited[n-1][m-1]=='*':
    print(-1)
else:
    print(visited[-1][-1])