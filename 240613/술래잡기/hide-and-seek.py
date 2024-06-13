import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# 게임 설정 변수 초기화
n, m, h, k = map(int, input().split())  # 격자 크기, 도망자 수, 나무 수, 턴 수 입력
change_direction = [(0, 0), (n // 2, n // 2)]  # 술래 방향 전환 지점 리스트
runner_dict = {}  # 도망자 정보를 담을 딕셔너리
runner_map = [[[] for _ in range(n)] for _ in range(n)]  # 각 위치에 있는 도망자 ID 리스트
tree_map = [[0] * n for _ in range(n)]  # 나무 위치 정보
score = 0  # 술래 점수
# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 도망자 클래스
class Runner:
    def __init__(self, id, r, c, d):  # 생성자: ID, 위치(r, c), 방향(d) 설정
        self.id = id
        self.r = r
        self.c = c
        self.d = d

    def get_next(self):  # 다음 이동할 위치 반환
        return self.r + dr[self.d], self.c + dc[self.d]

    def change_dir(self):  # 방향 반대로 변경
        self.d = (self.d + 2) % 4

# 술래 클래스
class Catcher:
    def __init__(self, r, c, d):  # 생성자: 위치(r, c), 방향(d) 설정
        self.r = r
        self.c = c
        self.d = d
        self.flag = True  # 방향 전환 플래그 (True: 바깥쪽, False: 안쪽)

    def move(self):  # 한 칸 이동 후 위치 반환
        self.r += dr[self.d]
        self.c += dc[self.d]
        return self.r, self.c

# 술래 방향 전환 지점 설정
for i in range(n // 2):  # 0부터 (n // 2 - 1)까지 반복 (격자 중심에서 바깥쪽으로 이동)
    change_direction.append((max(n // 2 - i - 1, 0), n // 2 - i))
    change_direction.append((n // 2 - i - 1, n // 2 + i + 1))
    change_direction.append((n // 2 + i + 1, n // 2 + i + 1))
    change_direction.append((n // 2 + i + 1, n // 2 - i - 1))

# 도망자 정보 입력 및 초기화
for i in range(m):
    r, c, d = map(int, input().split())  # 위치, 이동 방법 입력
    if d == 1:  # 좌우 이동
        d = 1  # 동쪽
    else:  # 상하 이동
        d = 2  # 북 쪽
    runner_dict[i + 1] = Runner(i + 1, r - 1, c - 1, d)  # 도망자 객체 생성
    runner_map[r - 1][c - 1].append(i + 1)  # 위치 정보에 도망자 ID 추가

# 나무 정보 입력
for _ in range(h):
    r, c = map(int, input().split())
    tree_map[r - 1][c - 1] = -1  # 나무 위치 표시

# 술래 객체 생성
catcher = Catcher(n // 2, n // 2, 0)  # 처음에는 북쪽으로 이동

# 도망자 이동 함수
def move_runner():
    for rid, runner in runner_dict.items():
        if abs(catcher.r - runner.r) + abs(catcher.c - runner.c) <= 3:
            next_r, next_c = runner.get_next()
            if not (0 <= next_r < n and 0 <= next_c < n):
                runner.change_dir()
                next_r, next_c = runner.get_next()
            if (next_r, next_c) != (catcher.r, catcher.c):
                runner_map[runner.r][runner.c].remove(runner.id)
                runner.r, runner.c = next_r, next_c
                runner_map[runner.r][runner.c].append(runner.id)

# 술래 이동 함수
def move_catcher():
    a, b = catcher.r, catcher.c
    r, c = catcher.move()

    if (r, c) in change_direction:
        if r < n // 2:
            if c > n // 2:
                if catcher.flag:
                    catcher.d = 2  # 남쪽
                else:
                    catcher.d = 3  # 서쪽
            else:
                if catcher.flag:
                    catcher.d = 1  # 동쪽
                else:
                    catcher.d = 2  # 남쪽
        else:
            if c >= n // 2:
                if catcher.flag:
                    catcher.d = 3  # 서쪽
                else:
                    catcher.d = 0  # 북쪽
            else:
                if catcher.flag:
                    catcher.d = 0  # 북쪽
                else:
                    catcher.d = 1  # 동쪽

# 범위 확인 함수
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 술래가 도망자를 잡는 함수
def catch(t, score):
    r, c = catcher.r, catcher.c
    catch_runner = []

    for i in range(3):
        watch_r, watch_c = r + dr[catcher.d] * i, c + dc[catcher.d] * i
        if in_range(watch_r, watch_c):
            if tree_map[watch_r][watch_c] == 0 and runner_map[watch_r][watch_c]:
                runner_id_list = runner_map[watch_r][watch_c]
                for runner_id in runner_id_list:
                    catch_runner.append(runner_dict[runner_id])

    for runner in catch_runner:
        runner_map[runner.r][runner.c].remove(runner.id)
        del runner_dict[runner.id]

    return score + len(catch_runner) * t

# 술래의 방향 전환 함수
def rotate():
    if catcher.r == 0 and catcher.c == 0:
        catcher.d = 2  # 남쪽
        catcher.flag = False
    if catcher.r == n // 2 and catcher.c == n // 2:
        catcher.d = 0  # 북쪽
        catcher.flag = True

# 메인 게임 루프
t = 1
score = 0
while runner_dict and t <= k:
    move_runner()
    move_catcher()
    score = catch(t, score)
    rotate()
    t += 1

print(score)  # 최종 점수 출력