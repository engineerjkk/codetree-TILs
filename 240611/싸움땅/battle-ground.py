import sys
input = sys.stdin.readline

EMPTY = (-1, -1, -1, -1, -1, -1)
n, m, k = map(int, input().split())
gun = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        if nums[j] != 0:
            gun[i][j].append(nums[j])

class Player:
    def __init__(self, num, r, c, d, s, a=0):
        self.num = num
        self.r = r
        self.c = c
        self.d = d
        self.s = s
        self.a = a

    def __repr__(self):
        return f"Player({self.num}, {self.r}, {self.c}, {self.d}, {self.s}, {self.a})"

    def get_position(self):
        return self.r, self.c

    def update_position(self, nr, nc, d):
        self.r = nr
        self.c = nc
        self.d = d

    def update_stats(self, a):
        self.a = a

players = []
for i in range(m):
    r, c, d, s = map(int, input().split())
    players.append(Player(i, r-1, c-1, d, s))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
points = [0] * m

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def get_next(r, c, d):
    nr = r + dr[d]
    nc = c + dc[d]
    if not in_range(nr, nc):
        d = (d + 2) % 4
        nr = r + dr[d]
        nc = c + dc[d]
    return nr, nc, d

def find_player(pos):
    for player in players:
        if player.get_position() == pos:
            return player
    return EMPTY

def move(player, pos):
    nr, nc = pos
    gun[nr][nc].append(player.a)
    gun[nr][nc].sort(reverse=True)
    player.update_stats(gun[nr][nc][0])
    gun[nr][nc].pop(0)
    player.update_position(nr, nc, player.d)

def loser_move(player):
    gun[player.r][player.c].append(player.a)
    for i in range(4):
        ndir = (player.d + i) % 4
        nr = player.r + dr[ndir]
        nc = player.c + dc[ndir]
        if in_range(nr, nc) and find_player((nr, nc)) == EMPTY:
            player.update_position(player.r, player.c, ndir)
            player.update_stats(0)
            move(player, (nr, nc))
            break

def fight(p1, p2, pos):
    if (p1.s + p1.a, p1.s) > (p2.s + p2.a, p2.s):
        points[p1.num] += (p1.s + p1.a) - (p2.s + p2.a)
        loser_move(p2)
        move(p1, pos)
    else:
        points[p2.num] += (p2.s + p2.a) - (p1.s + p1.a)
        loser_move(p1)
        move(p2, pos)

def simulate():
    for player in players:
        nr, nc, ndir = get_next(player.r, player.c, player.d)
        next_player = find_player((nr, nc))
        player.update_position(nr, nc, ndir)
        if next_player == EMPTY:
            move(player, (nr, nc))
        else:
            fight(player, next_player, (nr, nc))

for _ in range(k):
    simulate()

print(*points)