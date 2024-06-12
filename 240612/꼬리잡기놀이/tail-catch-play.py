import sys
input = sys.stdin.readline
from collections import deque
N,M,K=map(int,input().split())
space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return -1<r<N and -1<c<N

teams=[]
for i in range(N):
    for j in range(N):
        if space[i][j]==1:
            queue=deque()
            queue.append((i,j))
            trace=deque()
            trace.append((i,j))
            visit=[[False]*N for _ in range(N)]
            visit[i][j]=True
            while queue:
                r,c=queue.popleft()
                for k in range(4):
                    nr=r+dr[k]
                    nc=c+dc[k]
                    if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]==2:
                        visit[nr][nc]=True
                        queue.append((nr,nc))
                        trace.append((nr,nc))
            r,c=trace[-1]
            for k in range(4):
                nr=r+dr[k]
                nc=c+dc[k]
                if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]==3:
                    trace.append((nr,nc))
                    break
            teams.append(trace)

def move():
    for team in teams:
        r,c=team.pop()
        space[r][c]=4
        space[team[-1][0]][team[-1][1]]=3
        r,c=team[0]
        space[r][c]=2
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and space[nr][nc]==4:
                space[nr][nc]=1
                team.appendleft((nr,nc))
    
def ball(idx):
    idx=idx%(4*N)
    if idx<N:
        for c in range(N):
            if space[idx][c] in (1,2,3):
                return (idx,c)
    elif idx<2*N:
        for r in reversed(range(N)):
            if space[r][idx-N] in (1,2,3):
                return (r,idx-N)
    elif idx<3*N:
        for c in reversed(range(N)):
            if space[3*N-1-idx][c] in (1,2,3):
                return (3*N-1-idx,c)
    else:
        for r in range(N):
            if space[r][4*N-1-idx] in (1,2,3):
                return (r,4*N-1-idx)
    return (-1,-1)

def change(r,c):
    if (r,c)==(-1,-1):
        return 0
    for i in range(M):
        if (r,c) in teams[i]:
            for j in range(len(teams[i])):
                if teams[i][j]==(r,c):
                    space[teams[i][0][0]][teams[i][0][1]]=3
                    space[teams[i][-1][0]][teams[i][-1][1]]=1
                    teams[i].reverse()
                    return (j+1)**2

cnt=0
for i in range(K):
    move()
    a,b=ball(i)
    cnt+=change(a,b)
print(cnt)