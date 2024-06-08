from collections import deque

# 변수 선언 및 입력:
n, m, k = tuple(map(int, input().split()))
# 현재 포탑들이 가진 힘과 언제 각성했는지 기록해줍니다.
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
rec=[[0]*m for _ in range(n)] 


drcs = [0, 1, 0, -1], [1, 0, -1, 0]
drcs2 = [0, 0, 0, -1, -1, -1, 1, 1, 1], [0, -1, 1, 0, -1, 1, 0, -1, 1]

turn = 0

# 빛의 공격을 할 때 방문 여부와 경로 방향을 기록해줍니다.
vis=[[0]*m for _ in range(n)]
back_r=[[0]*m for _ in range(n)]
back_c=[[0]*m for _ in range(n)]

# 공격과 무관했는지 여부를 저장합니다.
is_active=[[False]*m for _ in range(n)]


# 구조체 turret을 정의해 관리합니다.
class Turrent:
    def __init__(self, c, r, rec, p):
        self.c = c
        self.r = r
        self.rec = rec
        self.p = p


# 살아있는 포탑들을 관리합니다.
live_turret = []


# 턴을 진행하기 전 필요한 전처리를 정리해줍니다.
def init():
    global turn
    
    turn += 1
    for i in range(n):
        for j in range(m):
            vis[i][j] = False
            is_active[i][j] = False


# 각성을 진행합니다.
# 각성을 하면 가장 약한 포탑이 n + m만큼 강해집니다.
def awake():
    # 우선순위에 맞게 현재 살아있는 포탑들을 정렬해줍니다.
    live_turret.sort(key=lambda x : (x.p, -x.rec, -(x.c + x.r), -x.r))

    # 가장 약한 포탑을 찾아 n + m만큼 더해주고,
    # is_active와 live_turret 배열도 갱신해줍니다.
    weak_turret = live_turret[0]
    c = weak_turret.c
    r = weak_turret.r

    board[c][r] += n + m
    rec[c][r] = turn
    weak_turret.p = board[c][r]
    weak_turret.rec = rec[c][r]
    is_active[c][r] = True

    live_turret[0] = weak_turret


# 레이저 공격을 진행합니다.
def laser_attack():
    # 기존에 정렬된 가장 앞선 포탑이
    # 각성한 포탑입니다.
    weak_turret = live_turret[0]
    sc = weak_turret.c
    sr = weak_turret.r
    power = weak_turret.p

    # 기존에 정렬된 가장 뒤 포탑이
    # 각성한 포탑을 제외한 포탑 중 가장 강한 포탑입니다.
    strong_turret = live_turret[-1]
    ec = strong_turret.c
    er = strong_turret.r

    # bfs를 통해 최단경로를 관리해줍니다.
    q = deque()
    vis[sc][sr] = True
    q.append((sc, sr))

    # 가장 강한 포탑에게 도달 가능한지 여부를 can_attack에 관리해줍니다.
    can_attack = False

    while q:
        c, r = q.popleft()

        # 가장 강한 포탑에게 도달할 수 있다면
        # 바로 멈춥니다.
        if c == ec and r == er:
            can_attack = True
            break

        # 각각 우, 하, 좌, 상 순서대로 방문하며 방문 가능한 포탑들을 찾고
        # queue에 저장해줍니다.
        for dc, dr in zip(drcs[0], drcs[1]):
            nc = (c + dc + n) % n
            nr = (r + dr + m) % m

            # 이미 방문한 포탑이라면 넘어갑니다.
            if vis[nc][nr]: 
                continue

            # 벽이라면 넘어갑니다.
            if board[nc][nr] == 0: 
                continue

            vis[nc][nr] = True
            back_c[nc][nr] = c
            back_r[nc][nr] = r
            q.append((nc, nr))

    # 만약 도달 가능하다면 공격을 진행합니다.
    if can_attack:
        # 우선 가장 강한 포탑에게는 power만큼의 공격을 진행합니다.
        board[ec][er] -= power
        if board[ec][er] < 0: 
            board[ec][er] = 0
        is_active[ec][er] = True

        # 기존의 경로를 역추적하며
        # 경로 상에 있는 모든 포탑에게 power // 2만큼의 공격을 진행합니다.
        cc = back_c[ec][er]
        cr = back_r[ec][er]

        while not (cc == sc and cr == sr):
            board[cc][cr] -= power // 2
            if board[cc][cr] < 0: 
                board[cc][cr] = 0
            is_active[cc][cr] = True

            next_cc = back_c[cc][cr]
            next_cr = back_r[cc][cr]

            cc = next_cc
            cr = next_cr

    # 공격을 성공했는지 여부를 반환합니다.
    return can_attack


# 레이저 공격을 하지 못했다면 폭탄 공격을 진행합니다.
def bomb_attack():
    # 기존에 정렬된 가장 앞선 포탑이
    # 각성한 포탑입니다.
    weak_turret = live_turret[0]
    sc = weak_turret.c
    sr = weak_turret.r
    power = weak_turret.p

    # 기존에 정렬된 가장 뒤 포탑이
    # 각성한 포탑을 제외한 포탑 중 가장 강한 포탑입니다.
    strong_turret = live_turret[-1]
    ec = strong_turret.c
    er = strong_turret.r

    # 가장 강한 포탑의 3 * 3 범위를 모두 탐색하며
    # 각각에 맞는 공격을 진행합니다.
    for dc2, dr2 in zip(drcs2[0], drcs2[1]):
        nc = (ec + dc2 + n) % n
        nr = (er + dr2 + m) % m

        # 각성한 포탑 자기 자신일 경우 넘어갑니다.
        if nc == sc and nr == sr: 
            continue

        # 가장 강한 포탑일 경우 pow만큼의 공격을 진행합니다.
        if nc == ec and nr == er:
            board[nc][nr] -= power
            if board[nc][nr] < 0: 
                board[nc][nr] = 0
            is_active[nc][nr] = True
        # 그 외의 경우 pow // 2만큼의 공격을 진행합니다.
        else:
            board[nc][nr] -= power // 2
            if board[nc][nr] < 0: 
                board[nc][nr] = 0
            is_active[nc][nr] = True


# 공격에 관여하지 않은 모든 살아있는 포탑의 힘을 1 증가시킵니다.
def reserve():
    for i in range(n):
        for j in range(m):
            if is_active[i][j]: 
                continue
            if board[i][j] == 0: 
                continue   
            board[i][j] += 1

# k턴 동안 진행됩니다.
for _ in range(k):
    # 턴을 진행하기 전 살아있는 포탑을 정리합니다.
    live_turret = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                new_turret = Turrent(i, j, rec[i][j], board[i][j])
                live_turret.append(new_turret)

    # 살아있는 포탑이 1개 이하라면 바로 종료합니다.
    if len(live_turret) <= 1: 
        break

    # 턴을 진행하기 전 필요한 전처리를 정리해줍니다.
    init()

    # 각성을 진행합니다.
    awake()

    # 레이저 공격을 진행합니다.
    is_suc = laser_attack()
    # 레이저 공격을 하지 못했다면 포탄 공격을 진행합니다.
    if not is_suc: 
        bomb_attack()

    # 공격에 관여하지 않은 모든 살아있는 포탑의 힘을 1 증가시킵니다.
    reserve()

# 살아있는 포탑의 힘 중 가장 큰 값을 출력합니다.
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, board[i][j])

print(ans)