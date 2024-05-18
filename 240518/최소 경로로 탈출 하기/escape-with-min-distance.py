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

visited=[[0]*n for _ in range(n)]

cnt=1
while queue:
    r,c,cnt = queue.popleft()
    cnt+=1
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if -1<nr<n and -1<nc<n and lst[nr][nc]==1 and visited[nr][nc]==0:
            visited[nr][nc]=cnt
            queue.append((nr,nc,cnt))
visited[0][0]=0
# for i in range(n):
#     print(visited[i])

if visited[-1][-1]==0:
    print(-1)
else:
    print(visited[-1][-1])