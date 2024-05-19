import sys
input = sys.stdin.readline
from collections import deque

dr=[-2,-1,1,2,2,1,-1,-2]
dc=[1,2,2,1,-1,-2,-2,-1]

n = int(input())
r1,c1,r2,c2=tuple(map(int,input().split()))
r1-=1
c1-=1
r2-=1
c2-=1

visited=[[0]*n for _ in range(n)]

queue=deque()
cnt=0

queue.append((r1,c1,cnt))
visited[r1][c1]=cnt
while queue:
    r,c,cnt = queue.popleft()
    if r==r2 and c==c2:
        print(cnt)
        exit()
    cnt+=1
    for i in range(8):
        nr=r+dr[i]
        nc=c+dc[i]
        if -1<nr<n and -1<nc<n and visited[nr][nc]==0:
            visited[nr][nc]=cnt
            queue.append((nr,nc,cnt))
# for i in range(n):
#     print(visited[i])
print(-1)