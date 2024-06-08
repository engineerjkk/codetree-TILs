'''

가장 약한 포탑과 가장 강한 포탑 선정: 특정 조건에 따라 포탑을 정렬하여 선정합니다.
레이저 공격: BFS를 이용하여 최단 경로를 찾고, 경로 상의 포탑에 피해를 입힙니다.
포탄 공격: 지정된 범위의 포탑에 피해를 입힙니다.
포탑 정비: 공격에 참여하지 않은 포탑의 공격력을 증가시킵니다.
'''
from collections import deque

# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))  # 격자 크기 (n x m), 턴 수 (k) 입력
board = []  # 격자 정보 저장 (2차원 리스트)
for _ in range(n):
    board.append(list(map(int, input().split())))  # 격자 정보 입력 (공백 구분)
rec = [[0] * m for _ in range(n)]  # 각 포탑의 마지막 공격 턴 저장 (2차원 리스트)

drcs = [0, 1, 0, -1], [1, 0, -1, 0]  # 상하좌우 이동 방향 (델타 좌표)
drcs2 = [0, 0, 0, -1, -1, -1, 1, 1, 1], [0, -1, 1, 0, -1, 1, 0, -1, 1]  # 포탄 공격 범위

turn = 0  # 현재 턴

# 빛의 공격 관련 변수
vis = [[0] * m for _ in range(n)]  # 방문 여부 기록
back_r = [[0] * m for _ in range(n)]  # 레이저 경로 역추적용 (행)
back_c = [[0] * m for _ in range(n)]  # 레이저 경로 역추적용 (열)

# 공격 여부 기록
is_active = [[False] * m for _ in range(n)]  # 해당 턴에 공격에 참여했는지 여부


# 포탑 클래스 정의
# 포탑의 위치, 마지막 공격턴, 공격력 정보를 담는 클래스
class Turrent:
    def __init__(self, c, r, rec, p):
        self.c = c  # 포탑의 열 위치
        self.r = r  # 포탑의 행 위치
        self.rec = rec  # 포탑의 마지막 공격 턴
        self.p = p  # 포탑의 공격력


# 살아있는 포탑 리스트
live_turret = []


# 턴 초기화 함수
# 매 턴 시작 전에 방문 기록과 공격 참여 여부를 초기화
def init():
    global turn  # 전역 변수 turn 사용

    turn += 1  # 턴 증가
    for i in range(n):
        for j in range(m):
            vis[i][j] = False  # 방문 기록 초기화
            is_active[i][j] = False  # 공격 참여 여부 초기화


# 각성 함수: 가장 약한 포탑 선정 및 공격력 증가
# 가장 약한 포탑을 선정하고 공격력을 증가시킴. 포탑 정렬 기준은 문제에서 제시한 우선 순위를 따름
def awake():
    # 포탑 정렬 기준: 공격력(낮은 순), 마지막 공격 턴(최근 순), 행+열(큰 순), 열(큰 순)
    live_turret.sort(key=lambda x: (x.p, -x.rec, -(x.c + x.r), -x.r))  

    weak_turret = live_turret[0]  # 가장 약한 포탑
    c, r = weak_turret.c, weak_turret.r  # 가장 약한 포탑의 위치

    board[c][r] += n + m  # 공격력 증가 (n + m)
    rec[c][r] = turn  # 마지막 공격 턴 갱신
    weak_turret.p = board[c][r]  # 포탑 객체의 공격력 갱신
    weak_turret.rec = rec[c][r]  # 포탑 객체의 마지막 공격 턴 갱신
    is_active[c][r] = True  # 공격 참여 표시

    live_turret[0] = weak_turret  # 정렬된 리스트 갱신


# 레이저 공격 함수
# 1. BFS를 이용하여 공격자에서 가장 강한 포탑까지으 최단 경로를 찾음
# 2. 경로가 존재하면 경로 상의 포탑과 가장 강한 포탑에 피해를 입힘
# 3. 공격 성공 여부를 반환
def laser_attack():
    weak_turret = live_turret[0]  # 각성한 포탑 (공격자)
    sc, sr, power = weak_turret.c, weak_turret.r, weak_turret.p

    strong_turret = live_turret[-1]  # 가장 강한 포탑 (공격 대상)
    ec, er = strong_turret.c, strong_turret.r

    q = deque([(sc, sr)])  # BFS 큐 초기화 (공격자 위치)
    vis[sc][sr] = True  # 공격자 위치 방문 표시

    can_attack = False  # 레이저 공격 가능 여부

    while q:  # BFS 시작
        c, r = q.popleft()  # 현재 위치

        if c == ec and r == er:  # 공격 대상에 도달하면
            can_attack = True  # 공격 가능
            break

        for dc, dr in zip(drcs[0], drcs[1]):  # 상하좌우 탐색
            nc, nr = (c + dc + n) % n, (r + dr + m) % m  # 다음 위치 계산 (경계 처리)

            if vis[nc][nr] or board[nc][nr] == 0:  # 이미 방문했거나 벽이면 건너뜀
                continue

            vis[nc][nr] = True  # 방문 표시
            back_c[nc][nr] = c  # 경로 역추적 정보 저장
            back_r[nc][nr] = r
            q.append((nc, nr))  # 다음 위치 큐에 추가

    if can_attack:  # 공격 가능하면
        board[ec][er] -= power  # 공격 대상에 피해
        board[ec][er] = max(0, board[ec][er])  # 공격력 음수 방지
        is_active[ec][er] = True  # 공격 참여 표시

        cc, cr = back_c[ec][er], back_r[ec][er]  # 경로 역추적 시작

        while not (cc == sc and cr == sr):  # 공격자 위치까지 역추적
            board[cc][cr] -= power // 2  # 경로 상의 포탑에 피해
            board[cc][cr] = max(0, board[cc][cr])  # 공격력 음수 방지
            is_active[cc][cr] = True  # 공격 참여 표시

            cc, cr = back_c[cc][cr], back_r[cc][cr]  # 다음 역추적 위치

    return can_attack  # 공격 성공 여부 반환


# 폭탄 공격 함수
# 가장 강한 포탑과 주변 8개 포탑에 피해를 입힘
def bomb_attack():
    weak_turret = live_turret[0]  # 각성한 포탑 (공격자)
    sc, sr, power = weak_turret.c, weak_turret.r, weak_turret.p

    strong_turret = live_turret[-1]  # 가장 강한 포탑 (공격 대상)
    ec, er = strong_turret.c, strong_turret.r

    for dc2, dr2 in zip(drcs2[0], drcs2[1]):  # 폭탄 공격 범위 탐색
        nc, nr = (ec + dc2 + n) % n, (er + dr2 + m) % m  # 폭탄 범위 계산 (경계 처리)

        if nc == sc and nr == sr:  # 각성한 포탑은 제외
            continue

        if nc == ec and nr == er:  # 공격 대상 포탑
            board[nc][nr] -= power  # 공격력만큼 피해
        else:  # 주변 포탑
            board[nc][nr] -= power // 2  # 공격력의 절반만큼 피해

        board[nc][nr] = max(0, board[nc][nr])  # 공격력 음수
        is_active[nc][nr] = True  # 공격 참여 표시


# 포탑 정비 함수: 공격에 참여하지 않은 포탑의 공격력 증가
# 공격에 참여하지 않은 포탑의 공격력을 1증가시킴
def reserve():
    for i in range(n):
        for j in range(m):
            if not is_active[i][j] and board[i][j] > 0:  # 공격에 참여하지 않고 살아있는 포탑
                board[i][j] += 1  # 공격력 1 증가


# 메인 게임 루프 (k 턴 동안 반복)
# 1. k 턴 동안 반복하며, 매 턴마다 init, awake, laser_attack 또는 bomb_attack, reserve 함수를 순서대로 실행함.
# 2. 살아있는 포탑이 1개 이하가 되면 게임을 종료
for _ in range(k):
    # 살아있는 포탑 정보 갱신
    live_turret = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:  # 살아있는 포탑이면
                new_turret = Turrent(i, j, rec[i][j], board[i][j])  # 포탑 객체 생성
                live_turret.append(new_turret)  # 살아있는 포탑 리스트에 추가

    if len(live_turret) <= 1:  # 살아있는 포탑이 1개 이하이면 종료
        break

    init()  # 턴 초기화 (방문 기록, 공격 참여 여부 초기화)
    awake()  # 각성 (가장 약한 포탑 선정 및 공격력 증가)

    is_suc = laser_attack()  # 레이저 공격 시도
    if not is_suc:  # 레이저 공격 실패 시
        bomb_attack()  # 폭탄 공격

    reserve()  # 포탑 정비 (공격에 참여하지 않은 포탑 공격력 증가)


# 게임 종료 후 가장 강한 포탑 찾기
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, board[i][j])  # 최대 공격력 갱신

print(ans)  # 가장 강한 포탑의 공격력 출력