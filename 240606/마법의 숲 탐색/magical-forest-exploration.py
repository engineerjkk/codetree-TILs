import sys
input = sys.stdin.readline
from collections import deque
MAX=70
space=[[0]*MAX for _ in range(MAX+3)]
Exit=[[False]*MAX for _ in range(MAX+3)]
R,C,K=map(int,input().split())
answer=0
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def cango(r,c):
    flag = -1<r-1 and r+1<R+3 and -1<c-1 and c+1<C
    flag = flag and space[r-1][c-1]==0 and space[r-1][c]==0 and space[r-1][c+1]==0
    flag = flag and space[r][c-1]==0 and space[r][c]==0 and space[r][c+1]==0
    flag = flag and space[r+1][c]==0
    return flag

def resetMap():
    for i in range(R+3):
        for j in range(C):
            space[i][j]=0
            Exit[i][j]=False

def in_range(r,c):
    return 2<r<R+3 and -1<c<C

def bfs(r,c):
    visit=[[False]*MAX for _ in range(MAX+3)]
    queue=deque()
    queue.append((r,c))
    visit[r][c]=True
    result=r
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if not visit[nr][nc] and in_range(nr,nc) and (space[nr][nc]==space[r][c] or (space[nr][nc]!=0 and Exit[r][c]==True)):
                visit[nr][nc]=True
                queue.append((nr,nc))
                result=max(result,nr)
    return result


def down(r,c,d,id):
    if cango(r+1,c):
        down(r+1,c,d,id)
    elif cango(r+1,c-1):
        down(r+1,c-1,(d+3)%4,id)
    elif cango(r+1,c+1):
        down(r+1,c+1,(d+1)%4,id)
    else:
        if (not in_range(r-1,c-1) and not in_range(r-1,c) and not in_range(r-1,c+1)) or not in_range(r-1,c):
            resetMap()
        else:
            space[r][c]=id
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                space[nr][nc]=id
            Exit[r+dr[d]][c+dc[d]]=True
            global answer
            answer+=bfs(r,c)-3+1


for id in range(1,K+1):
    c,d=map(int,input().split())
    down(0,c-1,d,id)
print(answer)