import sys
input = sys.stdin.readline
N,M,K=map(int,input().split())

space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))
guns=[[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if space[i][j]>0:
            guns[i][j].append(space[i][j])
points=[0]*M
empty=(-1,-1,-1,-1,-1,-1)
dr=[-1,0,1,0]
dc=[0,1,0,-1]

class Player:
    def __init__(self,id,r,c,d,power,gun=0):
        self.id=id
        self.r=r
        self.c=c
        self.d=d
        self.power=power
        self.gun=gun
    def get_next(self):
        return self.r+dr[self.d],self.c+dc[self.d]
    def change_dir(self):
        self.d=(self.d+2)%4

players=[]
for i in range(M):
    r,c,d,power=map(int,input().split())
    players.append(Player(i,r-1,c-1,d,power))

def in_range(r,c):
    return -1<r<N and -1<c<N

def find_player(r,c):
    for player in players:
        if player.r==r and player.c==c:
            return player
    return empty

def move(player,nr,nc):
    guns[nr][nc].append(player.gun)
    guns[nr][nc].sort(reverse=True)
    player.gun=guns[nr][nc][0]
    guns[nr][nc].pop(0)
    player.r,player.c=nr,nc

def loser_move(player):
    guns[player.r][player.c].append(player.gun)
    player.gun=0
    for i in range(4):
        nd=(player.d+i)%4
        nr=player.r+dr[nd]
        nc=player.c+dc[nd]
        if in_range(nr,nc) and find_player(nr,nc)==empty:
            player.r,player.c,player.d=nr,nc,nd
            move(player,nr,nc)
            return

def fight(p1,p2,nr,nc):
    if (p1.power+p1.gun,p1.power)>(p2.power+p2.gun,p2.power):
        points[p1.id]+=(p1.power+p1.gun)-(p2.power+p2.gun)
        loser_move(p2)
        move(p1,nr,nc)
    else:
        points[p2.id]+=(p2.power+p2.gun)-(p1.power+p1.gun)
        loser_move(p1)
        move(p2,nr,nc)

def simulate():
    for player in players:
        nr,nc=player.get_next()
        if not in_range(nr,nc):
            player.change_dir()
            nr,nc=player.get_next()
        next_player=find_player(nr,nc)
        player.r,player.c=nr,nc
        if next_player==empty:
            move(player,nr,nc)
        else:
            fight(player,next_player,nr,nc)

for _ in range(K):
    simulate()
print(*points)