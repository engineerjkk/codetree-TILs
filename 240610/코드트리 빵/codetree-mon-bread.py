import sys
from collections import deque
MAX=sys.maxsize
empty=(-1,-1)
n,m=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
gs25=[]
for _ in range(m):
    r,c=map(int,input().split())
    gs25.append((r-1,c-1))

people=[empty]*m
time=0
dr=[-1,0,0,1]
dc=[0,-1,1,0]
step=[[0]*n for _ in range(n)]
visit=[[False]*n for _ in range(n)]

def in_range(r,c):
    return -1<r<n and -1<c<n

def bfs(start_pos):
    for r in range(n):
        for c in range(n):
            visit[r][c]=False
            step[r][c]=0
    queue=deque()
    queue.append(start_pos)
    sr,sc=start_pos
    visit[sr][sc]=True
    step[sr][sc]=0
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
        if people[i]==empty or people[i]==gs25[i]:
            continue
        #베이스캠프에서 출발
        bfs(gs25[i]) #편의점까리의 최단거리를 구함
        r,c=people[i]
        min_distance=MAX
        min_r,min_c=-1,-1
        for j in range(4):
            nr=r+dr[j]
            nc=c+dc[j]
            if in_range(nr,nc) and visit[nr][nc] and step[nr][nc]<min_distance:
                min_distance=step[nr][nc]
                min_r,min_c=nr,nc
        people[i]=(min_r,min_c)
    for i in range(m):
        if people[i]==gs25[i]:
            r,c=people[i]
            space[r][c]=-1
    if time>m:#시간을 초과하면 여기까지만,
        return

    #이제 위에서 스킵됐던 사람을 베이스캠프로 옮기는것.
    bfs(gs25[time-1])
    min_distance=MAX
    min_r,min_c=-1,-1
    for r in range(n):
        for c in range(n):
            if visit[r][c] and space[r][c]==1 and step[r][c]<min_distance:
                min_distance=step[r][c]
                min_r,min_c=r,c
    people[time-1]=(min_r,min_c)
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