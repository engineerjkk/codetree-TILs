import sys
input = sys.stdin.readline
from collections import deque
n,m,k = map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
recent=[[0]*m for _ in range(n)]
visit=[[0]*m for _ in range(n)]
back=[[0]*m for _ in range(n)]
is_active=[[False]*m for _ in range(n)]
dr=[0,1,0,-1]
dc=[1,0,-1,0]
dr2=[-1,-1,0,1,1,1,0,-1]
dc2=[0,1,1,1,0,-1,-1,-1]
turn=0

class Turrent:
    def __init__(self,r,c,recent,power):
        self.r=r
        self.c=c
        self.recent=recent
        self.power=power

def init():
    global turn
    turn+=1
    for i in range(n):
        for j in range(m):
            visit[i][j]=False
            is_active[i][j]=False

def awake():
    live_turret.sort(key=lambda x:(x.power,-x.recent,-(x.r+x.c),-x.c))
    weak_turret=live_turret[0]
    r=weak_turret.r
    c=weak_turret.c
    board[r][c]+=m+n
    recent[r][c]=turn
    weak_turret.recent=recent[r][c]
    weak_turret.power=board[r][c]
    is_active[r][c]=True

def laser_attack():
    weak_turret=live_turret[0]
    sr=weak_turret.r
    sc=weak_turret.c
    power=weak_turret.power
    strong_turret=live_turret[-1]
    er=strong_turret.r
    ec=strong_turret.c
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
            if not visit[nr][nc] and board[nr][nc]>0:
                visit[nr][nc]=True
                back[nr][nc]=(r,c)
                queue.append((nr,nc))
    if can_attack:
        board[er][ec]-=power
        board[er][ec]=max(0,board[er][ec])
        is_active[er][ec]=True
        cr,cc=back[er][ec]
        while True:
            if cr==sr and cc==sc:
                break
            board[cr][cc]-=power//2
            board[cr][cc]=max(0,board[cr][cc])
            cr,cc=back[cr][cc]
            is_active[cr][cc]=True
    return can_attack

def bomb_attack():
    weak_turret=live_turret[0]
    sr,sc,power=weak_turret.r,weak_turret.c,weak_turret.power
    strong_turret=live_turret[-1]
    er,ec=strong_turret.r,strong_turret.c
    board[er][ec]-=power
    board[er][ec]=max(0,board[er][ec])
    is_active[er][ec]=True
    for i in range(8):
        nr=(er+dr2[i]+n)%n
        nc=(ec+dc2[i]+m)%m
        if not (sr==nr and sc==nc):
            board[nr][nc]-=power//2
            board[nr][nc]=max(0,board[nr][nc])
            is_active[nr][nc]=True

def reserve():
    for i in range(n):
        for j in range(m):
            if not is_active[i][j] and board[i][j]>0:
                board[i][j]+=1

for _ in range(k):
    live_turret=[]
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                new_turret=Turrent(i,j,recent[i][j],board[i][j])
                live_turret.append(new_turret)
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
        ans=max(ans,board[i][j])
print(ans)