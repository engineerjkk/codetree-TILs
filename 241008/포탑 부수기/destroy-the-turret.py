import sys
input = sys.stdin.readline
from collections import deque

n,m,k=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
recent=[[0]*m for _ in range(n)]
back=[[0]*m for _ in range(n)]
is_active=[[0]*m for _ in range(n)]
visit=[[False]*m for _ in range(n)]
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
    for i in range(n):
        for j in range(m):
            is_active[i][j]=False
            back[i][j]=0
            visit[i][j]=False
    return

def awake():
    global turn
    turn+=1
    live_turret.sort(key=lambda x:(x.power,-(x.recent),-(x.r+x.c),-x.c))
    weak_turret=live_turret[0]
    sr,sc,power=weak_turret.r,weak_turret.c,weak_turret.power
    space[sr][sc]+=n+m
    recent[sr][sc]=turn
    weak_turret.power=space[sr][sc]
    weak_turret.recent=recent[sr][sc]
    is_active[sr][sc]=True
    return 

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
        if r==er and c==ec:
            can_attack=True
            break
        for i in range(4):
            nr=(r+dr[i]+n)%n
            nc=(c+dc[i]+m)%m
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
            if cr==sr and cc==sc:
                break
            space[cr][cc]-=power//2
            space[cr][cc]=max(0,space[cr][cc])
            cr,cc=back[cr][cc]
            is_active[cr][cc]=True
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
        nr=(er+dr2[i]+n)%n
        nc=(ec+dc2[i]+m)%m
        if not(sr==nr and sc==nc):
            space[nr][nc]-=power//2
            space[nr][nc]=max(0,space[nr][nc])
            is_active[nr][nc]=True
    return 

def reserve():
    for i in range(n):
        for j in range(m):
            if space[i][j]>0 and not is_active[i][j]:
                space[i][j]+=1

for _ in range(k):
    live_turret=[]
    for i in range(n):
        for j in range(m):
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

ans=0
for i in range(n):
    for j in range(m):
        if space[i][j]>0:
            ans=max(ans,space[i][j])
print(ans)