from collections import deque

# 전역 변수들을 정의합니다.
MAX_N = 31
MAX_L = 41
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]
bef_k = [0 for _ in range(MAX_N)]
R = [0 for _ in range(MAX_N)]
C = [0 for _ in range(MAX_N)]
H = [0 for _ in range(MAX_N)]
W = [0 for _ in range(MAX_N)]
K = [0 for _ in range(MAX_N)]
nr = [0 for _ in range(MAX_N)]
nc = [0 for _ in range(MAX_N)]
dmg = [0 for _ in range(MAX_N)]
is_moved = [False for _ in range(MAX_N)]


# 움직임을 시도해봅니다.
def try_movement(idx, dir):
    queue = deque()
    is_pos = True

    # 초기화 작업입니다.
    for i in range(1, N + 1):
        dmg[i] = 0
        is_moved[i] = False
        nr[i] = R[i]
        nc[i] = C[i]

    queue.append(idx)
    is_moved[idx] = True

    while queue:
        r = queue.popleft()

        nr[r] += dr[dir]
        nc[r] += dc[dir]

        # 경계를 벗어나는지 체크합니다.
        if nr[r] < 1 or nc[r] < 1 or nr[r] + H[r] - 1 > L or nc[r] + W[r] - 1 > L:
            return False

        # 대상 조각이 다른 조각이나 장애물과 충돌하는지 검사합니다.
        for i in range(nr[r], nr[r] + H[r]):
            for j in range(nc[r], nc[r] + W[r]):
                if info[i][j] == 1:
                    dmg[r] += 1
                if info[i][j] == 2:
                    return False

        # 다른 조각과 충돌하v는 경우, 해당 조각도 같이 이동합니다.
        for i in range(1, N + 1):
            if is_moved[i] or K[i] <= 0:
                continue
            if R[i] > nr[r] + H[r] - 1 or nr[r] > R[i] + H[i] - 1:
                continue
            if C[i] > nc[r] + W[r] - 1 or nc[r] > C[i] + W[i] - 1:
                continue

            is_moved[i] = True
            queue.append(i)

    dmg[idx] = 0
    return True


# 특정 조각을 지정된 방향으로 이동시키는 함수입니다.
def move_piece(idx, move_dir):
    if K[idx] <= 0:
        return

    # 이동이 가능한 경우, 실제 위치와 체력을 업데이트합니다.
    if try_movement(idx, move_dir):
        for i in range(1, N + 1):
            R[i] = nr[i]
            C[i] = nc[i]
            K[i] -= dmg[i]


# 입력값을 받습니다.
L, N, Q = map(int, input().split())
for i in range(1, L + 1):
    info[i][1:] = map(int, input().split())
for i in range(1, N + 1):
    R[i], C[i], H[i], W[i], K[i] = map(int, input().split())
    bef_k[i] = K[i]

for _ in range(Q):
    idx, d = map(int, input().split())
    move_piece(idx, d)

# 결과를 계산하고 출력합니다.
ans = sum([bef_k[i] - K[i] for i in range(1, N + 1) if K[i] > 0])
print(ans)