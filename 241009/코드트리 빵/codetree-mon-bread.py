import sys
input = sys.stdin.readline
from collections import deque

n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

gs25=[]
for _ in range(m):
    r,c=map(int,input().split())
    gs25.append((r-1,c-1))
step=[[0]*n for _ in range(n)]
visit=[[False]*n for _ in range(n)]
empty=(-1,-1)
people=[empty]*m
dr=[-1,0,0,1]
dc=[0,-1,1,0]

def in_range(r,c):
    return -1<r<n and -1<c<n

def end():
    for i in range(m):
        if people[i]!=gs25[i]:
            return False
    return True

def bfs(pos):
    for i in range(n):
        for j in range(n):
            step[i][j]=0
            visit[i][j]=False
    r,c=pos
    visit[r][c]=True
    step[r][c]=0
    queue=deque()
    queue.append((r,c))
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]!=-1:
                queue.append((nr,nc))
                visit[nr][nc]=True
                step[nr][nc]=step[r][c]+1
    return 


def simulate(time):
    for i in range(m):
        if people[i]==empty or people[i]==gs25[i]:
            continue
        bfs(gs25[i])
        r,c=people[i]
        min_r,min_c=-1,-1
        distance=sys.maxsize
        for j in range(4):
            nr=r+dr[j]
            nc=c+dc[j]
            if in_range(nr,nc) and visit[nr][nc] and step[nr][nc]<distance:
                distance=step[nr][nc]
                min_r,min_c=nr,nc
        people[i]=(min_r,min_c)
    
    for i in range(m):
        if people[i]==gs25[i]:
            r,c=people[i]
            space[r][c]=-1
    
    if time>m:
        return 
    
    bfs(gs25[time-1])
    min_r,min_c=-1,-1
    distance=sys.maxsize
    for r in range(n):
        for c in range(n): 
            if space[r][c]==1 and visit[r][c] and step[r][c]<distance:
                distance=step[r][c]
                min_r,min_c=r,c
    people[time-1]=(min_r,min_c)
    space[min_r][min_c]=-1
    return 

time=0
while True:
    time+=1
    simulate(time)
    if end():
        break
print(time)