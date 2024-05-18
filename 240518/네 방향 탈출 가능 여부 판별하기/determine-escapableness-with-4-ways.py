import sys
input = sys.stdin.readline
from collections import deque
n,m = tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

visited=[[False]*m for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,1,0,-1]

queue=deque()
queue.append((0,0))
visited[0][0]==True

while queue:
    r,c=queue.popleft()
    if r==(n-1) and c==(m-1):
        print(1)
        exit()
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if -1<nr<n and -1<nc<m and not visited[nr][nc] and lst[nr][nc]==1:
            visited[nr][nc]=True
            queue.append((nr,nc))

print(0)