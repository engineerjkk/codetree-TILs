import sys
input = sys.stdin.readline
from collections import deque
n,m=map(int,input().split())
time=0
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
gs25=[]
for id in range(m):
    r,c=map(int,input().split())
    gs25.append([r-1,c-1])
people=[]
for _ in range(m):
    people.append([-1,-1])
time=0
MAX=sys.maxsize
dr=[-1,0,0,1]
dc=[0,-1,1,0]
step=[[0]*n for _ in range(n)]
visit=[[0]*n for _ in range(n)]

def in_range(r,c):
    return -1<r<n and -1<c<n

def bfs(pos):
    for i in range(n):
        for j in range(n):
            visit[i][j]=False
            step[i][j]=0
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
                step[nr][nc]=step[r][c]+1
                queue.append((nr,nc))

def simulate():
    
    for i in range(m):
        if people[i]==[-1,-1] or people[i]==gs25[i]:
            continue
        bfs(gs25[i])
        min_distance=MAX
        min_r,min_c=-1,-1
        r,c=people[i]
        for j in range(4):
            nr=r+dr[j]
            nc=c+dc[j]
            if in_range(nr,nc) and visit[nr][nc] and step[nr][nc]<min_distance:
                min_distance=step[nr][nc]
                min_r,min_c=nr,nc
        people[i]=[min_r,min_c]
    for i in range(m):
        if people[i]==gs25[i]:
            r,c=people[i]
            space[r][c]=-1   
    if time>m:
        return
    bfs(gs25[time-1])
    min_distance=MAX
    min_r,min_c=-1,-1
    for r in range(n):
        for c in range(n):
            if visit[r][c] and space[r][c]==1 and step[r][c]<min_distance:
                min_distance=step[r][c]
                min_r,min_c=r,c
    people[time-1]=[min_r,min_c]
    space[min_r][min_c]=-1

def end():
    for i in range(m):
        if people[i]!=gs25[i]:
            return False
    return True

while True:
    time+=1
    simulate()
    if end():
        break
print(time)