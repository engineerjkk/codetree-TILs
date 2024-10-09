import sys
input = sys.stdin.readline
from collections import deque

n,m,K=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

def in_range(r,c):
    return -1<r<n and -1<c<n

teams=[]
for i in range(n):
    for j in range(n):
        if space[i][j]==1:
            queue=deque()
            queue.append((i,j))
            trace=deque()
            trace.append((i,j))
            visit=[[False]*n for _ in range(n)]
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
                    break
            teams.append(trace)

def move():
    for team in teams:
        r,c=team.pop()
        space[r][c]=4
        space[team[-1][0]][team[-1][1]]=3#
        r,c=team[0]
        space[r][c]=2#
        for i in range(4):
            nr=r+dr[i]#
            nc=c+dc[i]#
            if in_range(nr,nc) and space[nr][nc]==4:
                space[nr][nc]=1
                team.appendleft((nr,nc))
                break

def ball(idx):
    idx=(idx)%(4*n)#

    if idx<n:
        for c in range(n):
            if space[idx][c] in (1,2,3):
                return (idx,c)
    elif idx<n*2:
        for r in reversed(range(n)):#
            if space[r][idx-n] in (1,2,3):
                return (r,idx-n)
    elif idx<n*3:
        for c in reversed(range(n)):#
            if space[3*n-1-idx][c] in (1,2,3):
                return (3*n-1-idx,c)#
    else:
        for r in range(n):
            if space[r][4*n-1-idx] in (1,2,3):
                return (r,4*n-1-idx)#
    return (-1,-1)

def catch(r,c):
    if (r,c)==(-1,-1):
        return 0
    for i in range(m):
        if (r,c) in teams[i]:
            for j in range(len(teams[i])):
                if teams[i][j]==(r,c):
                    space[teams[i][0][0]][teams[i][0][1]]=3
                    space[teams[i][-1][0]][teams[i][-1][1]]=1
                    teams[i].reverse()
                    return (j+1)**2                    

score=0
for i in range(K):
    move()
    a,b=ball(i)
    score+=catch(a,b)
print(score)