import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# 게임 설정 입력 받기
empty = (-1, -1, -1, -1, -1, -1)  # 빈 칸을 나타내는 튜플
n, m, k = map(int, input().split())  # 격자 크기, 플레이어 수, 라운드 수
gun = [[[] for _ in range(n)] for _ in range(n)]  # 격자 정보 (총 정보 저장)
for i in range(n):
    nums = list(map(int, input().split()))  # 각 행의 총 정보 입력
    for j in range(n):
        if nums[j] != 0:  # 빈 칸이 아니라면 총 정보 추가
            gun[i][j].append(nums[j])

# 플레이어 클래스 정의
class Player:
    def __init__(self, num, r, c, d, s, a=0):  # 플레이어 정보 초기화
        self.num = num  # 플레이어 번호
        self.r = r  # 행 위치
        self.c = c  # 열 위치
        self.d = d  # 방향 (0: ↑, 1: →, 2: ↓, 3: ←)
        self.s = s  # 초기 능력치
        self.a = a  # 총 공격력

    def __repr__(self):  # 플레이어 정보 출력 형식 지정
        return f"Player({self.num}, {self.r}, {self.c}, {self.d}, {self.s}, {self.a})"

    def get_position(self):  # 현재 위치 반환
        return self.r, self.c

    def update_position(self, nr, nc, d):  # 위치 및 방향 업데이트
        self.r = nr
        self.c = nc
        self.d = d

    def update_stats(self, a):  # 총 공격력 업데이트
        self.a = a

# 플레이어 정보 입력 받기
players = []  # 플레이어 객체 리스트
for i in range(m):
    r, c, d, s = map(int, input().split())
    players.append(Player(i, r - 1, c - 1, d, s))  # 0-based indexing

# 이동 방향 정의
dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌 (행 변화)
dc = [0, 1, 0, -1]  # 상, 우, 하, 좌 (열 변화)

points = [0] * m  # 각 플레이어의 포인트 초기화

# 범위 내에 있는지 확인하는 함수
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 다음 위치 계산 함수
def get_next(r, c, d):
    nr = r + dr[d]  # 다음 행 위치
    nc = c + dc[d]  # 다음 열 위치
    if not in_range(nr, nc):  # 범위를 벗어나면 반대 방향으로 이동
        d = (d + 2) % 4
        nr = r + dr[d]
        nc = c + dc[d]
    return nr, nc, d

# 특정 위치에 있는 플레이어 찾는 함수
def find_player(pos):
    for player in players:
        if player.get_position() == pos:  # 위치가 일치하면 해당 플레이어 반환
            return player
    return empty  # 없으면 빈 칸 정보 반환

# 이동 함수 (빈 칸으로 이동)
def move(player, pos):
    nr, nc = pos  # 이동할 위치
    gun[nr][nc].append(player.a)  # 현재 총을 해당 위치에 추가
    gun[nr][nc].sort(reverse=True)  # 공격력 내림차순 정렬
    player.update_stats(gun[nr][nc][0])  # 가장 강한 총 획득
    gun[nr][nc].pop(0)  # 획득한 총 제거
    #player.update_position(nr, nc, player.d)  # 위치 및 방향 업데이트

# 진 플레이어 이동 함수
def loser_move(player):
    gun[player.r][player.c].append(player.a)  # 현재 총을 해당 위치에 추가
    for i in range(4):  # 오른쪽으로 90도씩 회전하며 빈 칸 탐색
        ndir = (player.d + i) % 4  # 회전된 방향
        nr = player.r + dr[ndir]
        nc = player.c + dc[ndir]
        if in_range(nr, nc) and find_player((nr, nc)) == empty:  # 빈 칸이면 이동
            player.update_position(player.r, player.c, ndir)  # 방향 업데이트
            player.update_stats(0)  # 총 버림
            move(player, (nr, nc))  # 이동
            break

# 싸움 함수
def fight(p1, p2, pos):
    if (p1.s + p1.a, p1.s) > (p2.s + p2.a, p2.s):  # p1이 이긴 경우
        points[p1.num] += (p1.s + p1.a) - (p2.s + p2.a)  # 포인트 획득
        loser_move(p2)  # p2 이동
        move(p1, pos)  # p1 이동
    else:  # p2가 이긴 경우
        points[p2.num] += (p2.s + p2.a) - (p1.s + p1.a)  # 포인트 획득
        loser_move(p1)  # p1 이동
        move(p2, pos)  # p2 이동

# 시뮬레이션 함수 (1 라운드)
def simulate():
    for player in players:
        nr, nc, ndir = get_next(player.r, player.c, player.d)  # 다음 위치 계산
        next_player = find_player((nr, nc))  # 다음 위치에 있는 플레이어 확인
        player.update_position(nr, nc, ndir)  # 위치 및 방향 업데이트

        if next_player == empty:  # 빈 칸이면 이동
            move(player, (nr, nc))
        else:  # 플레이어가 있으면 싸움
            fight(player, next_player, (nr, nc))

# 시뮬레이션 시작 (k 라운드)
for _ in range(k):
    simulate()

# 결과 출력
print(*points)  # 각 플레이어의 포인트 출력