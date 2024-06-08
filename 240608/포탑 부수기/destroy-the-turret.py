import sys
input = sys.stdin.readline
from collections import deque
n,m,k = tuple(map(int,input().split()))
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
recent=[[0]*m for _ in range(n)]
dr=[-1,0,1,0]
dc=[0,1,0,-1]
#dr2=[0,-1,-1,0,1,1,1,0,-1]
#dc2=[0,0,1,1,1,0,-1,-1,-1]

dr2=[0,0,0,-1,-1,-1,1,1,1]
dc2=[0,-1,1,0,-1,1,0,-1,1]
turn=0
visit=[[0]*m for _ in range(n)]
back_r=[[0]*m for _ in range(n)]
back_c=[[0]*m for _ in range(n)]
is_active=[[False]*m for _ in range(n)]

class Turrent:
    def __init__(self,r,c,recent,power):
        self.r=r
        self.c=c
        self.recent=recent
        self.power=power

live_turret=[]

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
    board[r][c]+=n+m
    recent[r][c]=turn
    weak_turret.power=board[r][c]
    weak_turret.recent=recent[r][c]
    is_active[r][c]=True
    live_turret[0]=weak_turret

def laser_attack():
    weak_turret=live_turret[0]
    sr=weak_turret.r
    sc=weak_turret.c
    power=weak_turret.power
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
            
            if not visit[nr][nc] and board[nr][nc]>0:
                visit[nr][nc]=True
                back_r[nr][nc]=r
                back_c[nr][nc]=c
                queue.append((nr,nc))
    if can_attack:
        board[er][ec]-=power
        board[er][ec]=max(0,board[er][ec])
        is_active[er][ec]=True
        cr,cc=back_r[er][ec],back_c[er][ec]
        while not (cr==sr and cc==sc):
            board[cr][cc]-=power//2
            board[cr][cc]=max(0,board[cr][cc])
            is_active[cr][cc]=True
            next_cr=back_r[cr][cc]
            next_cc=back_c[cr][cc]
            cr=next_cr
            cc=next_cc
    return can_attack   

def bomb_attack():
    weak_turret=live_turret[0]
    sr,sc,power=weak_turret.r,weak_turret.c,weak_turret.power
    strong_turret=live_turret[-1]
    er,ec=strong_turret.r,strong_turret.c

    for i in range(9):
        nr=(er+dr2[i]+n)%n
        nc=(ec+dc2[i]+m)%m
        if not(nr==sr and nc==sc):
            if nr==er and nc==ec:
                board[nr][nc]-=power
            else:
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