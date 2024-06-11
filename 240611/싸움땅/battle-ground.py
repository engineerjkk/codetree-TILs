import sys
input = sys.stdin.readline

empty=(-1,-1,-1,-1,-1,-1)
n,m,k=map(int,input().split())
gun=[[[] for _ in range(n)] for _ in range(n)]
space=[]
for i in range(n):
    space.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if space[i][j]!=0:
            gun[i][j].append(space[i][j])

class Player:
    def __init__(self, id, r, c, d, power, gun=0):
        self.id = id
        self.r = r
        self.c = c
        self.d = d
        self.power = power
        self.gun = gun
        
players = []
for id in range(m):
    r, c, d, power = map(int, input().split())
    players.append(Player(id, r-1, c-1, d, power))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
points = [0] * m

def in_range(r, c):
    return -1 < r < n and -1 < c < n

def get_next(r, c, d):
    nr = r + dr[d]
    nc = c + dc[d]
    if not in_range(nr, nc):
        d = (d + 2) % 4
        nr = r + dr[d]
        nc = c + dc[d]
    return nr, nc, d

def find_player(nr, nc):
    for player in players:
        if player.r == nr and player.c == nc:
            return player
    return empty

def move(player, nr, nc):
    gun[nr][nc].append(player.gun)
    gun[nr][nc].sort(reverse=True)
    player.gun = gun[nr][nc][0]
    gun[nr][nc].pop(0)
    player.r = nr
    player.c = nc

def loser_move(player):
    gun[player.r][player.c].append(player.gun)
    for i in range(4):
        nd = (player.d + i) % 4
        nr = player.r + dr[nd]
        nc = player.c + dc[nd]
        if in_range(nr, nc) and find_player(nr, nc) == empty:
            player.r, player.c, player.d = nr, nc, nd
            player.gun = 0
            move(player, nr, nc)
            return

def fight(p1, p2, nr, nc):
    if (p1.power + p1.gun, p1.power) > (p2.power + p2.gun, p2.power):
        points[p1.id] += (p1.power + p1.gun) - (p2.power + p2.gun)
        loser_move(p2)
        move(p1, nr, nc)
    else:
        points[p2.id] += (p2.power + p2.gun) - (p1.power + p1.gun)
        loser_move(p1)
        move(p2, nr, nc)

def simulate():
    for player in players:
        nr, nc, nd = get_next(player.r, player.c, player.d)
        next_player = find_player(nr, nc)
        player.r, player.c, player.d = nr, nc, nd
        if next_player == empty:
            move(player, nr, nc)
        else:
            fight(player, next_player, nr, nc)

for _ in range(k):
    simulate()
print(*points)