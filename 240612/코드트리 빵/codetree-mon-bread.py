import sys
input = sys.stdin.readline
from collections import deque
N,M=map(int,input().split())
space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))
gs25=[]
for _ in range(M):
    r,c=map(int,input().split())
    gs25.append((r-1,c-1))
step=[[0]*N for _ in range(N)]
visit=[[False]*N for _ in range(N)]
dr=[-1,0,0,1]
dc=[0,-1,1,0]
empty=(-1,-1)
people=[empty]*M
time=0

def in_range(r,c):
    return -1<r<N and -1<c<N

def bfs(pos):
    for i in range(N):
        for j in range(N):
            step[i][j]=0
            visit[i][j]=False
    r,c=pos
    queue=deque()
    queue.append((r,c))
    visit[r][c]=True
    step[r][c]=0
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]!=-1:
                visit[nr][nc]=True
                queue.append((nr,nc))
                step[nr][nc]=step[r][c]+1

def move():
    for i in range(M):
        if people[i]==empty or people[i]==gs25[i]:
            continue
        bfs(gs25[i])
        distance=sys.maxsize
        min_r,min_c=-1,-1
        r,c=people[i]
        for j in range(4):
            nr=r+dr[j]
            nc=c+dc[j]
            if in_range(nr,nc) and visit[nr][nc] and step[nr][nc]<distance:
                distance=step[nr][nc]
                min_r=nr
                min_c=nc
        people[i]=(min_r,min_c)
    for i in range(M):
        if people[i]==gs25[i]:
            r,c=people[i]
            space[r][c]=-1
    if time>M:
        return
    bfs(gs25[time-1])
    distance=sys.maxsize
    min_r,min_c=-1,-1
    for r in range(N):
        for c in range(N):
            if visit[r][c] and space[r][c]==1 and step[r][c]<distance:
                distance=step[r][c]
                min_r,min_c=r,c 
    people[time-1]=(min_r,min_c)
    space[min_r][min_c]=-1

def end():
    for i in range(M):
        if people[i]!=gs25[i]:
            return False
    return True

while True:
    time+=1
    move()
    if end():
        break
print(time)