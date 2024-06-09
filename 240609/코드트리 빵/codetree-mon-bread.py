import sys

from collections import deque

input = sys.stdin.readline
'''
고려할 것
0. 편의점에 도착하거나, 베이스캠프 도달 시 -1 처리
1. 최단 경로에 있는 베이스캠프 or CU가 X가 되는 경우
 - 신경쓰지 말고, 이동할 때는 항상 BFS로 찾기
2. 모두 이동 후 X가 됨
3. 이동 후 베이스캠프에 배치
4. 사람 이동 : 상 좌 우 하 / 베이스캠프 찾기 : 행이 작은 -> 열이 작은
5. 그래서 사람 이동은?
 - board에 쓰기 / 리스트 하나 만들기 => 리스트를 만들어야 같은 위치 판단 가능.
6. 도착 판단 : people과 board가 같으면 continue
'''

# 모든 사람이 편의점에 도착했는지 확인하는 함수
def all_arrived():
    for i in range(M):
        #사람 i의 현재 위치가 목표 편의점과 같지 않으면 False 변환
        if cu[i][0] != people[i][0] or cu[i][1] != people[i][1]:
            return False
    return True

#특정 번호의 사람을 베이스 캠프에 배치하는 함수
def set_people(number):
    queue = deque()
    #목표 편의점 위치에서 BFS를 시작
    queue.append((cu[number][0], cu[number][1], 0))
    visited = [[False] * N for _ in range(N)]
    candidate = []  # 베이스캠프 후보

    while queue:
        r, c, d = queue.popleft()
        #현재 위치가 베이스캠프라면 후보 리스트에 추가
        if space[r][c] == 1:
            candidate.append((d, r, c))
        #상,좌,우,하 순서로 인접한 칸을 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr,nc) and not visited[nr][nc] and space[nr][nc]!=-1:
                queue.append((nr, nc, d + 1))
                visited[nr][nc] = True
    #후보들 중 가장 우선 순위가 높은 베이스캠프를 선택
    candidate.sort(key=lambda x: (x[0], x[1], x[2]))  # 거리, 행, 열 순으로 오름차순 정렬
    r, c = candidate[0][1], candidate[0][2]
    people[number][0], people[number][1] = r, c
    space[r][c] = -1#해당 베이스캠프는 더 이상 사용할 수 없음

    return

# 격자 내 위치가 유효한지 확인하는 함수
def in_range(r, c):
    return -1<r<N and -1<c<N

#특정 번호의 사람을 위해 목표 편의점까지의 경로를 생성하는 함수
def make_route(number, r, c):
    global route

    queue = deque()
    queue.append((r, c, []))
    visited = [[False] * N for _ in range(N)]

    while queue:
        r, c, lst = queue.popleft()
        #목표 편의점에 도달한 경우 경로를 저장
        if r == cu[number][0] and c == cu[number][1]:
            route[number] = lst
            break
        #상,좌,우,하 순서로 인접한 칸을 탐색
        for i in range(4):  # 상, 좌, 우, 하 순
            nr = r + dr[i]
            nc = c + dc[i]
            #범위를 벗어나거나 이미 방문했거나 지나갈 수 없는 경우 건너뜀
            if in_range(nr,nc) and not visited[nr][nc] and space[nr][nc]!=-1:
                queue.append((nr, nc, lst + [(nr, nc)]))
                visited[nr][nc] = True
    return

#모든 사람을 한 칸씩 이동시키는 함수
def move_people():
    for i in range(M):
        r, c = people[i][0], people[i][1]
        # 아직 출발 안했거나, 편의점에 도착한 친구면 놔둠
        if (r == -1 and c == -1) or (r == cu[i][0] and c == cu[i][1]):
            continue

        if not route[i]:  # 아직 경로가 정해지지 않은 친구면 정해줌
            make_route(i, r, c)
        else:
            for rr, rc in route[i]:
                if space[rr][rc] == -1:  # 만약 원래의 경로가 막혔다면
                    make_route(i, r, c)  # 다시 경로를 생성
                    break

        # 경로 지정이 다 끝났다면, 경로대로 움직임
        people[i][0] = route[i][0][0]
        people[i][1] = route[i][0][1]
        route[i] = route[i][1:]

    for i in range(M):
        r, c = people[i][0], people[i][1]

        if r == -1 and c == -1:
            break
        if cu[i][0] == r and cu[i][1] == c:  # 편의점에 도착했다면, -1 처리
            space[r][c] = -1

    return


N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
people, cu = [], []
for _ in range(M):
    r, c = map(int, input().split())
    cu.append((r - 1, c - 1))
    people.append([-1, -1])

#초기화
route = [[] for _ in range(M)]
dr=[-1,0,0,1]
dc=[0,-1,1,0]
time = 0
#모든 사람이 편의점에 도착할 때까지 반복
while not all_arrived():
    move_people()  # 격자에 있는 사람 모두 움직임
    if time < M:  # 베이스캠프에 사람 놓기/t번 사람이 베이스캠프에 도착
        set_people(time)
    time += 1

print(time)