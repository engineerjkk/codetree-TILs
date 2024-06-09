import sys
from collections import deque

INT_MAX = sys.maxsize
EMPTY = (-1, -1)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 0이면 빈 칸, 1이면 베이스 캠프, 2라면 아무도 갈 수 없는 곳을 뜻합니다.
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 편의점 목록을 관리합니다.
cvs_list = []
for _ in range(m):
    r, c = tuple(map(int, input().split()))  # x, y를 r, c로 변경
    cvs_list.append((r - 1, c - 1))         # x, y를 r, c로 변경

# 현재 사람들의 위치를 관리합니다.
# 초기 사람들은 격자 밖에 있으므로
# 위치를 EMPTY 상태로 놓습니다.
people = [EMPTY] * m

# 현재 시간을 기록합니다.
curr_t = 0

# drs, dcs값을 
# 문제에서의 우선순위인 상좌우하 순으로 적어줍니다.
drs = [-1, 0, 0, 1]
dcs = [ 0, -1, 1, 0]

# bfs에 사용되는 변수들입니다.
# 최단거리 결과 기록
step = [
    [0] * n
    for _ in range(n)
]
# 방문 여부 표시
visited = [
    [False] * n
    for _ in range(n)
]


# (r, c)가 격자 내에 있는 좌표인지를 판단합니다.
def in_range(r, c):  # x, y를 r, c로 변경
    return 0 <= r and r < n and 0 <= c and c < n  # x, y를 r, c로 변경


# (r, c)로 이동이 가능한지 판단합니다.
def can_go(r, c):  # x, y를 r, c로 변경
    # 범위를 벗어나지 않으면서, 방문했던 적이 없으면서, 이동 가능한 곳이어야 합니다.
    return in_range(r, c) and not visited[r][c] and grid[r][c] != 2  # x, y를 r, c로 변경


# start_pos를 시작으로 하는 BFS를 진행합니다.
# 시작점으로부터의 최단거리 결과는 step배열에 기록됩니다.
def bfs(start_pos):
    # visited, step 값을 전부 초기화합니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0
    
    # 초기 위치를 넣어줍니다.
    q = deque()
    q.append(start_pos)
    sr, sc = start_pos  # sx, sy를 sr, sc로 변경
    visited[sr][sc] = True  # sx, sy를 sr, sc로 변경
    step[sr][sc] = 0      # sx, sy를 sr, sc로 변경

    # BFS를 진행합니다.
    while q:
        # 가장 앞에 원소를 골라줍니다.
        r, c = q.popleft()  # x, y를 r, c로 변경

        # 인접한 칸을 보며 아직 방문하지 않은 칸을 큐에 넣어줍니다.
        for dr, dc in zip(drs, dcs):  # dxs, dys를 drs, dcs로 변경
            nr, nc = r + dr, c + dc  # nx, ny를 nr, nc로 변경
            # 갈 수 있는 경우에만 진행합니다.
            if can_go(nr, nc):  # nx, ny를 nr, nc로 변경
                visited[nr][nc] = True  # nx, ny를 nr, nc로 변경
                step[nr][nc] = step[r][c] + 1  # nx, ny를 nr, nc로 변경
                q.append((nr, nc))  # nx, ny를 nr, nc로 변경


# 시뮬레이션을 진행합니다.
def simulate():
    # Step 1. 격자에 있는 사람들에 한하여 편의점 방향을 향해 1칸 움직입니다.
    for i in range(m):
        # 아직 격자 밖에 있는 사람이거나 이미 편의점에 도착한 사람이라면 패스합니다.
        if people[i] == EMPTY or people[i] == cvs_list[i]:
            continue
        
        # 원래는 현재 위치에서 편의점 위치까지의 최단거리를 구해줘야 합니다.
        # 다만 최단거리가 되기 위한 그 다음 위치를 구하기 위해서는
        # 거꾸로 편의점 위치를 시작으로 현재 위치까지 오는 최단거리를 구해주는 것이 필요합니다.
        # 따라서 편의점 위치를 시작으로 하는 BFS를 진행합니다.
        bfs(cvs_list[i])

        pr, pc = people[i]  # px, py를 pr, pc로 변경
        # 현재 위치에서 상좌우하 중 최단거리 값이 가장 작은 곳을 고르면
        # 그 곳으로 이동하는 것이 최단거리 대로 이동하는 것이 됩니다.
        # 그러한 위치 중 상좌우하 우선순위대로 가장 적절한 곳을 골라줍니다.
        min_dist = INT_MAX
        min_r, min_c = -1, -1  # min_x, min_y를 min_r, min_c로 변경
        for dr, dc in zip(drs, dcs):  # dxs, dys를 drs, dcs로 변경
            nr, nc = pr + dr, pc + dc  # nx, ny를 nr, nc로 변경
            if in_range(nr, nc) and visited[nr][nc] and min_dist > step[nr][nc]:  # nx, ny를 nr, nc로 변경
                min_dist = step[nr][nc]  # nx, ny를 nr, nc로 변경
                min_r, min_c = nr, nc  # min_x, min_y를 min_r, min_c로 변경

        # 우선순위가 가장 높은 위치로 한 칸 움직여줍니다.
        people[i] = (min_r, min_c)  # min_x, min_y를 min_r, min_c로 변경

    # Step 2. 편의점에 도착한 사람에 한하여 
    #        앞으로 이동 불가능하다는 표시로 
    #        grid값을 2로 바꿔줍니다.
    for i in range(m):
        if people[i] == cvs_list[i]:
            pr, pc = people[i]  # px, py를 pr, pc로 변경
            grid[pr][pc] = 2    # px, py를 pr, pc로 변경

    # Step 3. 현재 시간 curr_t에 대해 curr_t ≤ m를 만족한다면
    #        t번 사람이 베이스 캠프로 이동합니다.

    # curr_t가 m보다 크다면 패스합니다.
    if curr_t > m:
        return
    
    # Step 3-1. 편의점으로부터 가장 가까운 베이스 캠프를 고르기 위해
    #          편의점을 시작으로 하는 BFS를 진행합니다.
    bfs(cvs_list[curr_t - 1])

    # Step 3-2. 편의점에서 가장 가까운 베이스 캠프를 선택합니다.
    #          i, j가 증가하는 순으로 돌리기 때문에
    #          가장 가까운 베이스 캠프가 여러 가지여도
    #          알아서 (행, 열) 우선순위대로 골라집니다.
    min_dist = INT_MAX
    min_r, min_c = -1, -1  # min_x, min_y를 min_r, min_c로 변경
    for i in range(n):
        for j in range(n):
            # 방문 가능한 베이스 캠프 중
            # 거리가 가장 가까운 위치를 찾아줍니다.
            if visited[i][j] and grid[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_r, min_c = i, j  # min_x, min_y를 min_r, min_c로 변경

    # 우선순위가 가장 높은 베이스 캠프로 이동합니다.
    people[curr_t - 1] = (min_r, min_c)  # min_x, min_y를 min_r, min_c로 변경
    # 해당 베이스 캠프는 앞으로 이동이 불가능한 칸임을 표시합니다.
    grid[min_r][min_c] = 2  # min_x, min_y를 min_r, min_c로 변경

def end():
    # 단 한 사람이라도
    # 편의점에 도착하지 못했다면
    # 아직 끝나지 않은 것입니다.
    for i in range(m):
        if people[i] != cvs_list[i]:
            return False
    # 전부 편의점에 도착했다면 끝입니다.
    return True

while True:
    curr_t += 1
    simulate()
    # 전부 이동이 끝났다면 종료합니다.
    if end(): 
        break

print(curr_t)