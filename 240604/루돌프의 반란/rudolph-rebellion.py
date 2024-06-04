import sys

input = sys.stdin.readline
'''
1. 루돌프의 움직임
 - 아래, 오른, 왼, 위 순으로 움직임, bfs로 찾음.
 - 8번 계산해서 가까운 방향으로 이동

2. 충돌 확인
 - 산타가 있으면 산타를 C만큼 밀어버리고, 점수를 주고, 기절시킴
 - 밀린 곳에 산타가 있으면 상호작용

3. 산타의 움직임
 - 각 산타별로 루돌프와 가까운 위치로 이동 (상우하좌 순)
 - 해당 위치에 루돌프 있으면 밀림
 - 밀린 곳에 산타가 있으면 상호작용

4. 산타의 상태에 따라 1점씩 부여

5. 게임이 끝났는지 체크
'''

#특정 위치에 산타가 있는지 확인하는 함수
def check_santa(r, c):
    for i in range(P):
        if r == santas[i][0] and c == santas[i][1]:
            return i #산타번호 리턴
    return -1 #산타가 없으면 -1 리턴

#특정 위치가 게임판 범위 내에 있는지 확인하는 함수
def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False

#루돌프가 산타를 향해 이동하는 방향 계산 함수
def rudolf_to_santa(r1, c1, r2, c2):
    r, c = 0, 0
    if r2 - r1 != 0:
        r = (r2 - r1) // abs(r2 - r1) #행 방향이동 (-1,0,1)
    if c2 - c1 != 0:
        c = (c2 - c1) // abs(c2 - c1) #열 방향이동 (-1,0,1)

    return r, c

#산타가 루돌프를 향해 이동하는 방향 계산 함수
def santa_to_rudolf(r1, c1, r2, c2):
    distance = (r1 - r2) * (r1 - r2) + (c1 - c2) * (c1 - c2) #현재거리계산
    drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]#상우하좌
    ret_r, ret_c = 0, 0#반환할 이동방향초기화

    for dr, dc in drc:
        nr = r1 + dr
        nc = c1 + dc
        #범위밖이거나 다른 산타가 있으면 이동 불가
        if not in_range(nr, nc) or check_santa(nr, nc) != -1:
            continue

        tmp = (nr - r2) * (nr - r2) + (nc - c2) * (nc - c2)#이동 후 거리 계산
        if distance > tmp: #더가까워지는방향으로 업데이트
            ret_r, ret_c = dr, dc
            distance = tmp

    return ret_r, ret_c

#루돌프 이동함수
def move_rudolf():
    #가장 가까운 산타정보(산타번호,행,열,거리)
    s_info = [0, 0, 0, sys.maxsize]  # 산타 번호, r, c, 거리
    #가장 가까운 산타찾기
    for i in range(P):
        if status[i] == -1:#탈락한 산타는 무시
            continue
        #거리계산
        tmp = (rudolf[0] - santas[i][0]) * (rudolf[0] - santas[i][0]) + (rudolf[1] - santas[i][1]) * (
                rudolf[1] - santas[i][1])

        if tmp < s_info[3]:#더 가까운 산타 발견시 업데이트
            s_info = [i, santas[i][0], santas[i][1], tmp]
        elif tmp == s_info[3]:#거리가같을경우,행/열 우선순위로판단
            if s_info[1] < santas[i][0]:
                s_info = [i, santas[i][0], santas[i][1], tmp]
            elif s_info[1] == santas[i][0] and s_info[2] < santas[i][1]:
                s_info = [i, santas[i][0], santas[i][1], tmp]
    #루돌프 이동 방향 계산 및 이동
    cr, cc = rudolf_to_santa(rudolf[0], rudolf[1], santas[s_info[0]][0], santas[s_info[0]][1])
    rudolf[0] += cr
    rudolf[1] += cc

    check_collision(cr, cc, C)#충돌확인
    return

#산타이동함수
def move_santa(number):
    #루돌프 향해 이동방향 계산
    sr, sc = santa_to_rudolf(santas[number][0], santas[number][1], rudolf[0], rudolf[1])
    santas[number][0] += sr
    santas[number][1] += sc
    #루돌프와 충돌시
    if santas[number][0] == rudolf[0] and santas[number][1] == rudolf[1]:
        push_santa(number, -sr, -sc, D)#산타밀어내기
        score[i] += D
        if status[i] != -1:  # 퇴장되지 않았다면 기절
            status[i] = 2

    return

#산타밀어내기함수(재귀적으로 연쇄충돌처리)
def push_santa(number, cr, cc, power):
    #범위밖으로벗어나면탈락
    if not in_range(santas[number][0] + cr * power, santas[number][1] + cc * power):
        santas[number][0] += cr * power
        santas[number][1] += cc * power
        status[number] = -1
        return
    #밀려난위치에산타있는지확인
    s = check_santa(santas[number][0] + cr * power, santas[number][1] + cc * power)
    if s != -1:
        push_santa(s, cr, cc, 1)#연쇄충돌처리(다음산타밀어내기)

    santas[number][0] += cr * power#산타위치업ㄷ베이트
    santas[number][1] += cc * power

    return

#충돌확인함수
def check_collision(cr, cc, power):
    for i in range(P):
        #루돌프와산타
        if rudolf[0] == santas[i][0] and rudolf[1] == santas[i][1]:
            push_santa(i, cr, cc, power)#산타밀어내기
            score[i] += power
            if status[i] != -1:  # 퇴장되지 않았다면 기절
                status[i] = 2
            break

    return

#게임설정입력
N, M, P, C, D = map(int, input().split())  # 게임판 크기, 게임 턴 수, 산타 수, 루돌프 힘, 산타 힘
rudolf = list(map(int, input().split()))
rudolf[0] -= 1#좌표0부터시작하도록 조정
rudolf[1] -= 1
#산타위치정보리스트
santas = [[0] * 2 for _ in range(P)]

for _ in range(P):
    n, r, c = map(int, input().split())#산타번호,행,열입력
    santas[n - 1][0], santas[n - 1][1] = r - 1, c - 1#좌표0부터시작하도록조정
#점수및상태정보초기화 
#score:산타별점수, status산타별상태(0:정상,양수:기절턴수,-1:탈락)
score, status = [0] * P, [0] * P  # 양의 정수면 기절 카운트, -1이면 탈락
dr, dc = [1, 0, 0, -1], [0, 1, -1, 0]#이동방향 : 하우좌상

# Solution
for _ in range(M):#M턴 동안 반복
    move_rudolf()  # 루돌프 이동
    for i in range(P):
        if status[i] == 0:#기절상태가아니면이동
            move_santa(i)  # 산타 이동

    for i in range(P):
        if status[i] != -1:  # 퇴장 아니면
            score[i] += 1#점수증가
            status[i] = max(0, status[i] - 1)  # 기절 시간 줄임(0또는 음수면 기절해제)
    #게임종료조건확인
    for i in range(P):
        if status[i] != -1:#탈락하지않은산타가있으면 계속진행
            break
    else:#모든산타가 탈락했으면 종료
        break
print(*score)