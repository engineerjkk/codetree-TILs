import sys
input = sys.stdin.readline
from collections import deque

n, k = tuple(map(int,input().split()))
lst_n=[]
for _ in range(n):
    lst_n.append(list(map(int,input().split())))

lst_k=[]
for _ in range(k):
    lst_k.append(list(map(int,input().split())))


cnt=0

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def bfs(r,c):
    global cnt
    queue=deque()
    visited=[[False]*(n) for _ in range(n)]
    visited[r][c]=True
    queue.append((r,c))
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n and visited[nr][nc]==False and lst_n[nr][nc] == 0:
                visited[nr][nc]=True
                lst_n[nr][nc]=1
                queue.append((nr,nc))
                cnt+=1

for a,b in lst_k:
    bfs(a-1,b-1)

print(cnt)