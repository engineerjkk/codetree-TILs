import sys
input = sys.stdin.readline
from collections import deque

N,M=map(int,input().split())
space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))
step=[[0]*N for _ in range(N)]
visit=[[False]*N for _ in range(N)]
gs25=[]
for _ in range(M):
    r,c=map(int,input().split())
    gs25.append((r-1,c-1))

empty=(-1,-1)
people=[empty]*M

dr=[-1,0,0,1]
dc=[0,-1,1,0]

def in_range(r,c):
    return -1<r<N and -1<c<N

def bfs(pos):
    for r in range(N):
        for c in range(N):
            step[r][c]=0
            visit[r][c]=False
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


def move_people(t):
    for i in range(M):
        if people[i]==gs25[i] or people[i]==empty:
            continue

        bfs(gs25[i]) #
        distance=sys.maxsize
        min_r,min_c=-1,-1
        r,c=people[i]
        step[r][c]=0
        for j in range(4):
            nr=r+dr[j]
            nc=c+dc[j]
            if in_range(nr,nc) and visit[nr][nc] and space[nr][nc]!=-1 and step[nr][nc]<distance:
                distance=step[nr][nc]
                min_r,min_c=nr,nc
        people[i]=(min_r,min_c)
    
    for i in range(M):
        if people[i]==gs25[i]:
            r,c=people[i]
            space[r][c]=-1
    
    if t>M:
        return
    bfs(gs25[t-1])
    distance=sys.maxsize
    min_r,min_c=-1,-1
    for r in range(N):
        for c in range(N):
            if space[r][c]==1 and visit[r][c] and step[r][c]<distance:
                distance=step[r][c]
                min_r,min_c=r,c
    people[t-1]=(min_r,min_c) #
    space[min_r][min_c]=-1

def end():
    for i in range(M):
        if people[i]!=gs25[i]:
            return False
    return True
        


time=0
while True:
    time+=1
    move_people(time)
    if end():
        break
print(time)