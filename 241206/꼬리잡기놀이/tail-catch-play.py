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

visit=[[False]*N for _ in range(N)]

teams=[]
for i in range(N):
    for j in range(N):
        if space[i][j]==1:
            queue=deque()
            queue.append((i,j))
            trace=deque()
            trace.append((i,j))
            visit[i][j]=True
            while queue:
                r,c=queue.popleft()
                for k in range(4):
                    nr=r+dr[k]
                    nc=c+dc[k]
                    if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]==2:
                        queue.append((nr,nc))
                        trace.append((nr,nc))
                        visit[nr][nc]=True
            r,c=trace[-1]
            for k in range(4):
                nr=r+dr[k]
                nc=c+dc[k]
                if in_range(nr,nc) and not visit[nr][nc] and space[nr][nc]==3:
                    trace.append((nr,nc))
            teams.append((trace))

def ball(idx):
    idx=(idx)%(4*N)#
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
            if space[3*N-idx-1][c] in (1,2,3):
                return (3*N-idx-1,c)
    else:
        for r in range(N):
            if space[r][4*N-idx-1] in (1,2,3):
                return (r,4*N-idx-1)
    return (-1,-1)

def catch(a,b):
    if (a,b)==(-1,-1):
        return 0
    for i in range(len(teams)):
        if (a,b) in teams[i]:
            for j in range(len(teams[i])):
                if teams[i][j]==(a,b):
                    space[teams[i][0][0]][teams[i][0][1]]=3
                    space[teams[i][-1][0]][teams[i][-1][1]]=1
                    teams[i].reverse()
                    return (j+1)**2

def move_traveler():
    for team in teams:
        r,c=team.pop()
        space[r][c]=4
        r,c=team[-1]
        space[r][c]=3
        r,c=team[0]
        space[r][c]=2
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and space[nr][nc]==4:
                space[nr][nc]=1
                team.appendleft((nr,nc))
                break
        
score=0
for i in range(K):
    move_traveler()
    a,b=ball(i)
    score+=catch(a,b)
print(score)