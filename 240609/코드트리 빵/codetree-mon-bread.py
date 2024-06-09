import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용
from collections import deque  # BFS 탐색에 사용할 큐 자료구조

# Person 클래스: 사람의 위치 정보 저장
class Person():
    def __init__(self, r, c):
        self.r = r  # 행 좌표
        self.c = c  # 열 좌표

# Cu 클래스: 편의점 위치 정보 저장
class Cu():
    def __init__(self, r, c):
        self.r = r  # 행 좌표
        self.c = c  # 열 좌표

# Candidate 클래스: 베이스캠프 후보 (거리, 위치) 정보 저장
class Candidate():
    def __init__(self, d, r, c):
        self.d = d  # 편의점으로부터의 거리
        self.r = r  # 행 좌표
        self.c = c  # 열 좌표

# 입력 받기
N, M = map(int, input().split())  # 격자 크기 N, 사람 수 M
space = []  # 격자 정보
for _ in range(N):
    space.append(list(map(int, input().split())))  # 격자 정보 입력 (0: 빈 공간, 1: 베이스캠프)

people = []  # 사람들 위치 정보
cu = []  # 편의점 위치 정보
for _ in range(M):
    r, c = map(int, input().split())  
    cu.append(Cu(r - 1, c - 1))  # 편의점 위치 저장 (0-based indexing)
    people.append(Person(-1, -1))  # 초기 사람 위치 (-1, -1)로 설정 (아직 베이스캠프에 없음)

route = [[] for _ in range(M)]  # 각 사람의 이동 경로 저장
dr = [-1, 0, 0, 1]  # 상하좌우 이동 방향 (델타 탐색)
dc = [0, -1, 1, 0]
time = 0  # 현재 시간

# 모든 사람이 편의점에 도착했는지 확인하는 함수
def all_arrived():
    for i in range(M):
        if cu[i].r != people[i].r or cu[i].c != people[i].c:  # 편의점과 사람 위치 비교
            return False
    return True

# 범위 안에 있는지 확인하는 함수
def in_range(r, c):
    return -1 < r < N and -1 < c < N

# 특정 사람의 최단 경로를 계산하는 함수 (BFS)
def make_route(number, r, c):
    global route
    queue = deque()
    queue.append((r, c, []))  # 현재 위치, 경로 정보 큐에 추가
    visited = [[False] * N for _ in range(N)]  # 방문 여부 저장

    while queue:  # BFS 탐색 시작
        r, c, lst = queue.popleft()
        if r == cu[number].r and c == cu[number].c:  # 편의점 도착 시 경로 저장 후 종료
            route[number] = lst
            break
        for i in range(4):  # 상하좌우 탐색
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr, nc) and not visited[nr][nc] and space[nr][nc] != -1:  # 이동 가능한 칸인지 확인
                queue.append((nr, nc, lst + [(nr, nc)]))  # 큐에 다음 위치 및 경로 정보 추가
                visited[nr][nc] = True  # 방문 처리

# 사람들을 이동시키는 함수
def move_people():
    for i in range(M):  # 각 사람에 대해
        r, c = people[i].r, people[i].c
        if (r == -1 and c == -1) or (r == cu[i].r and c == cu[i].c):  # 베이스캠프에 없거나 편의점에 도착한 경우 continue
            continue
        if not route[i]:  # 경로가 없는 경우 경로 계산
            make_route(i, r, c)
        else:  # 경로가 있는 경우
            for rr, rc in route[i]:  # 경로를 따라 이동
                if space[rr][rc] == -1:  # 이동 불가능한 칸인 경우 다시 경로 계산
                    make_route(i, r, c)
                    break
        people[i].r = route[i][0][0]  # 다음 위치로 이동
        people[i].c = route[i][0][1]
        route[i] = route[i][1:]  # 이동한 칸 제거

    for i in range(M):  # 편의점에 도착한 사람 처리
        r, c = people[i].r, people[i].c
        if r == -1 and c == -1:  # 베이스캠프에 없는 경우 break
            break
        if cu[i].r == r and cu[i].c == c:  # 편의점 도착 시 해당 칸 -1로 변경 (이동 불가)
            space[r][c] = -1
    return

# 특정 사람을 베이스캠프에 배치하는 함수 (BFS)
def set_people(number):
    queue = deque()
    queue.append((cu[number].r, cu[number].c, 0))  # 편의점 위치, 거리 큐에 추가
    visited = [[False] * N for _ in range(N)]
    candidate = []  # 베이스캠프 후보 저장
    while queue:
        r, c, d = queue.popleft()
        if space[r][c] == 1:  # 베이스캠프 발견 시 후보에 추가
            candidate.append(Candidate(d, r, c))
        for i in range(4):  # 상하좌우 탐색
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr, nc) and not visited[nr][nc] and space[nr][nc] != -1:  # 이동 가능한 칸인지 확인
                queue.append((nr, nc, d + 1))
                visited[nr][nc] = True
    candidate.sort(key=lambda x: (x.d, x.r, x.c))  # 거리, 행, 열 순으로 정렬
    r, c = candidate[0].r, candidate[0].c  # 가장 가까운 베이스캠프 선택
    people[number].r, people[number].c = r, c  # 사람 배치
    space[r][c] = -1  # 해당 칸 -1로 변경 (이동 불가)
    return

# 메인 루프
while not all_arrived():  # 모든 사람이 편의점에 도착할 때까지 반복
    move_people()  # 사람들 이동
    if time < M:  # 시간이 사람 수보다 작은 경우 (새로운 사람 베이스캠프 배치)
        set_people(time)
    time += 1  # 시간 증가

print(time)  # 결과 출력 (모든 사람이 편의점에 도착하는 시간)