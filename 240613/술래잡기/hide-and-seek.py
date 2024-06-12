import sys

class Runner:
    """도망자 클래스"""
    def __init__(self, id, r, c, d):
        """
        도망자 객체 초기화

        Args:
            id (int): 도망자 ID
            r (int): 행 위치 (0부터 시작)
            c (int): 열 위치 (0부터 시작)
            d (tuple): 이동 방향 ((0, 1)은 오른쪽, (1, 0)은 아래쪽)
        """
        self.id = id
        self.r = r
        self.c = c
        self.d = d

    def get_next(self):
        """다음 이동할 위치 계산"""
        return self.r + self.d[0], self.c + self.d[1]

    def change_dir(self):
        """이동 방향 반대로 변경"""
        self.d = (self.d[0] * -1, self.d[1] * -1)

    def __repr__(self):
        """객체 표현 문자열 반환 (디버깅용)"""
        return f"도망자{self.id}"

class Catcher:
    """술래 클래스"""
    def __init__(self, r, c, d):
        """
        술래 객체 초기화

        Args:
            r (int): 행 위치 (0부터 시작)
            c (int): 열 위치 (0부터 시작)
            d (tuple): 이동 방향 ((-1, 0)은 위쪽)
        """
        self.r = r
        self.c = c
        self.d = d
        self.flag = True  # 안쪽에서 바깥쪽으로 이동하는지 여부

    def move(self):
        """술래 이동"""
        self.r += self.d[0]
        self.c += self.d[1]
        return self.r, self.c

    def __repr__(self):
        """객체 표현 문자열 반환 (디버깅용)"""
        return f"술래 ({self.r}, {self.c}), 방향: {self.d}"

# 입력 받기
n, m, h, k = map(int, sys.stdin.readline().split())

# 술래 방향 전환 좌표 리스트
change_direction = [(0, 0), (n // 2, n // 2)]  # 초기값: 시작점, 중앙
# 도망자 정보 딕셔너리 {runner_id: Runner}
runner_dict = {}
# 도망자 위치 정보 맵 (2차원 리스트)
runner_map = []
for _ in range(n):
    row = []
    for _ in range(n):
        row.append([])  # 각 칸에 도망자 ID 리스트 저장
    runner_map.append(row)

# 나무 위치 정보 맵 (2차원 리스트)
tree_map = [[0] * n for _ in range(n)]
# 술래 점수
score = 0

# 술래 방향 전환 좌표 계산
for i in range(n // 2):
    # 달팽이 모양 이동 경로 계산
    change_direction.append((max(n // 2 - i - 1, 0), n // 2 - i))
    change_direction.append((n // 2 - i - 1, n // 2 + i + 1))
    change_direction.append((n // 2 + i + 1, n // 2 + i + 1))
    change_direction.append((n // 2 + i + 1, n // 2 - i - 1))

# 도망자 정보 입력 및 초기 위치 설정
for i in range(m):
    x, y, d = map(int, sys.stdin.readline().split())
    if d == 1:
        d = (0, 1)  # 오른쪽
    else:
        d = (1, 0)  # 아래쪽
    runner_dict[i + 1] = Runner(i + 1, x - 1, y - 1, d)  # 0부터 시작하도록 조정
    runner_map[x - 1][y - 1].append(i + 1)

# 나무 정보 입력
for _ in range(h):
    x, y = map(int, sys.stdin.readline().split())
    tree_map[x - 1][y - 1] = -1  # 나무 위치 표시

# 술래 객체 생성 (초기 위치: 중앙, 초기 방향: 위쪽)
catcher = Catcher(n // 2, n // 2, (-1, 0))

# 도망자 이동 함수
def move_runner():
    """
    상하, 좌우로만 이동

    [이동 조건]
    술래와 간격이 3 이하만 이동
    다음 칸 : 격자 내부
    - 다음 칸에 술래가 있으면 움직이지 않음
    - 술래 없으면 이동 (나무 상관X)
    다음 칸 : 격자 외부
    - 방향 바꾸기 -> 술래 없으면 1칸 이동
    """
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
    """
    달팽이 모양으로 이동

    1. 1칸 이동
    2. 방향 바꾸는 지점 -> 방향 바꾸기
    """
    a, b = catcher.r, catcher.c
    r, c = catcher.move()
    if (r, c) in change_direction:
        if r < n // 2:
            # 안 -> 밖: 우 -> 하
            # 밖 -> 안: 상 -> 좌
            if c > n // 2:
                catcher.d = (1, 0) if catcher.flag else (0, -1)
            # 안 -> 밖: 상 -> 우
            # 밖 -> 안: 좌 -> 하
            else:
                catcher.d = (0, 1) if catcher.flag else (1, 0)
        else:
            # 안 -> 밖: 하 -> 좌
            # 밖 -> 안: 우 -> 상
            if c >= n // 2:
                catcher.d = (0, -1) if catcher.flag else (-1, 0)
            # 안 -> 밖: 좌 -> 상
            # 밖 -> 안: 하 -> 우
            else:
                catcher.d = (-1, 0) if catcher.flag else (0, 1)

# 술래가 도망자 잡는 함수
def catch(t, score):
    """
    술래 위치부터 바라보는 방향으로 3칸 (1,2) + 우측 => (1,2), (1,3), (1,4)
    나무 뒤는 못 잡음
    t 턴 -> t * 잡은 도망자 수 만큼 점수 획득

    잡힌 도망자 제거
    """
    r, c = catcher.r, catcher.c
    catch_runner = []
    for i in range(3):
        watch_r, watch_c = r + catcher.d[0] * i, c + catcher.d[1] * i
        if 0 <= watch_r < n and 0 <= watch_c < n:
            if tree_map[watch_r][watch_c] == 0 and runner_map[watch_r][watch_c]:
                runner_id_list = runner_map[watch_r][watch_c]
                for runner_id in runner_id_list:
                    catch_runner.append(runner_dict[runner_id])

    for runner in catch_runner:
        runner_map[runner.r][runner.c].remove(runner.id)
        del runner_dict[runner.id]

    return score + len(catch_runner) * t

# 술래 방향 전환 함수 (모서리 또는 중앙 도착 시)
def rotate():
    if catcher.r == 0 and catcher.c == 0:
        catcher.d = (1, 0)
        catcher.flag = False

    if catcher.r == n // 2 and catcher.c == n // 2:
        catcher.d = (-1, 0)
        catcher.flag = True

# 메인 게임 루프
t = 1
score = 0
while runner_dict and t <= k:  # 도망자가 남아있고 턴이 k 이하일 동안 반복
    move_runner()
    move_catcher()
    score = catch(t, score)
    rotate()
    t += 1

# 최종 점수 출력
print(score)