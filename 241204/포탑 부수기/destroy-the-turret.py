import sys
input = sys.stdin.readline
from collections import deque

N,M,K=map(int,input().split())
space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))

recent=[[0]*M for _ in range(N)]
back=[[0]*M for _ in range(N)]
visit=[[False]*M for _ in range(N)]
is_active=[[False]*M for _ in range(N)]
turn=0
dr=[-1,0,1,0]
dc=[0,1,0,-1]
dr2=[-1,-1,0,1,1,1,0,-1]
dc2=[0,1,1,1,0,-1,-1,-1]

class Turrent:
    def __init__(self,r,c,recent,power):
        self.r=r
        self.c=c
        self.recent=recent
        self.power=power

def init():
    global turn
    turn+=1
    for i in range(N):
        for j in range(M):
            back[i][j]=0
            visit[i][j]=False
            is_active[i][j]=False

def awake():
    live_turret.sort(key=lambda x: (x.power,-x.recent,-(x.r+x.c),-x.c))
    weak_turret=live_turret[0]
    r,c,power=weak_turret.r,weak_turret.c,weak_turret.power
    space[r][c]+=N+M
    recent[r][c]=turn
    weak_turret.power=space[r][c]
    weak_turret.recent=recent[r][c]
    is_active[r][c]=True

def laser_attack():
    weak_turret=live_turret[0]
    sr,sc,power=weak_turret.r,weak_turret.c,weak_turret.power
    strong_turret=live_turret[-1]
    er,ec=strong_turret.r,strong_turret.c
    queue=deque()
    queue.append((sr,sc))
    visit[sr][sc]=True
    can_attack=False
    while queue:
        r,c=queue.popleft()
        if (r,c)==(er,ec):
            can_attack=True
        for i in range(4):
            nr=(r+dr[i]+N)%N
            nc=(c+dc[i]+M)%M
            if not visit[nr][nc] and space[nr][nc]>0:
                queue.append((nr,nc))
                visit[nr][nc]=True
                back[nr][nc]=(r,c)
    if can_attack:
        space[er][ec]-=power
        space[er][ec]=max(0,space[er][ec])
        is_active[er][ec]=True
        cr,cc=back[er][ec]
        while True:
            if (cr,cc)==(sr,sc):
                break
            space[cr][cc]-=power//2
            space[cr][cc]=max(0,space[cr][cc])
            is_active[cr][cc]=True
            cr,cc=back[cr][cc]
    return can_attack

def bomb_attack():
    weak_turret=live_turret[0]
    sr,sc,power=weak_turret.r,weak_turret.c,weak_turret.power
    strong_turret=live_turret[-1]
    er,ec=strong_turret.r,strong_turret.c
    space[er][ec]-=power
    space[er][ec]=max(0,space[er][ec])
    is_active[er][ec]=True
    for i in range(8):
        nr=(er+dr2[i]+N)%N
        nc=(ec+dc2[i]+M)%M
        if (sr,sc)!=(nr,nc) and space[nr][nc]>0:
            space[nr][nc]-=power//2
            space[nr][nc]=max(0,space[nr][nc])
            is_active[nr][nc]=True
    return 

def reserve():
    for i in range(N):
        for j in range(M):
            if space[i][j]>0 and not is_active[i][j]:
                space[i][j]+=1




for _ in range(K):
    live_turret=[]
    for i in range(N):
        for j in range(M):
            if space[i][j]>0:
                live_turret.append(Turrent(i,j,recent[i][j],space[i][j]))
    if len(live_turret)<=1:
        break
    init()
    awake()
    success=laser_attack()
    if not success:
        bomb_attack()
    reserve()

answer=0
for i in range(N):
    for j in range(M):
        answer=max(answer,space[i][j])
print(answer)