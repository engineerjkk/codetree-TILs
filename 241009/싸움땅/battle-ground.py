import sys
input = sys.stdin.readline

n,m,k=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
guns=[[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if space[i][j]>0:
            guns[i][j].append(space[i][j])
points=[0]*m
dr=[-1,0,1,0]
dc=[0,1,0,-1]
empty=(-1,-1,-1,-1,-1,-1)

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
for id in range(m):
    r,c,d,power=map(int,input().split())
    players.append(Player(id,r-1,c-1,d,power))#

def in_range(r,c):
    return -1<r<n and -1<c<n

def find_player(nr,nc):
    for player in players:
        if player.r==nr and player.c==nc:
            return player
    return empty

def move(player,nr,nc):
    guns[nr][nc].append(player.gun)
    guns[nr][nc].sort(reverse=True)
    player.gun=guns[nr][nc][0]
    guns[nr][nc].pop(0)
    player.r=nr
    player.c=nc

def move_loser(player):
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
        move_loser(p2)
        move(p1,nr,nc)
    else:
        points[p2.id]+=(p2.power+p2.gun)-(p1.power+p1.gun)
        move_loser(p1)
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

for _ in range(k):
    simulate()
print(*points)