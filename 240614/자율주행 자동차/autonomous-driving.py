import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
r, c, d = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
visit[r][c] = True

# 방향 벡터 (북, 동, 남, 서)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 큐 초기화
queue = deque([(r, c, d)])

# 시뮬레이션
while queue:
    r, c, d = queue.popleft()
    moved = False
    for _ in range(4):
        # 왼쪽 방향으로 전환
        nd = (d - 1 + 4) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        # 왼쪽 방향으로 갈 수 있는지 확인
        if space[nr][nc] == 0 and not visit[nr][nc]:
            visit[nr][nc] = True
            queue.append((nr, nc, nd))
            moved = True
            break
        else:
            d = nd
    # 4방향 모두 이동할 수 없었던 경우 후진 시도
    if not moved:
        br = r - dr[(d + 2) % 4]
        bc = c - dc[(d + 2) % 4]
        if space[br][bc] == 0:
            queue.append((br, bc, d))

# 방문한 칸의 수를 계산
ans = sum([1 for i in range(n) for j in range(m) if visit[i][j]])

# 결과 출력
print(ans)