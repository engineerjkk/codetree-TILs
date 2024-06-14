# 이동 방향 설정
dr = [-1, 0, 1, 0]   # 상하좌우 (팩맨 이동)
dc = [0, -1, 0, 1]
dr2 = [-1, -1, 0, 1, 1, 1, 0, -1]  # 8방향 (몬스터 이동)
dc2 = [0, -1, -1, -1, 0, 1, 1, 1]

# 입력 받기
M, T = map(int, input().split())  # 몬스터 수, 턴 수
R, C = map(int, input().split())  # 팩맨 초기 위치 (1-based)
R, C = R - 1, C - 1  # 0-based 좌표로 변환

# 몬스터 정보와 냄새 정보를 저장할 딕셔너리
monsters = {}  # 위치: [방향1, 방향2, ...] 형태로 저장
smells = {}  # 위치: 남은 턴 수

# 몬스터 정보 입력 받기
for _ in range(M):
    r, c, d = map(int, input().split())  # 몬스터 위치, 방향 (1-based)
    pos = (r - 1, c - 1)  # 0-based 좌표로 변환
    if pos in monsters:  # 이미 몬스터가 있는 위치라면
        monsters[pos].append(d - 1)  # 방향 추가 (0-based)
    else:  # 새로운 위치라면
        monsters[pos] = [d - 1]  # 리스트 생성

# 팩맨 이동 함수 (DFS 탐색)
def packman_move(level, prey_count, path, r, c):
    global max_prey  # 최대 사냥 정보를 저장하는 전역 변수
    if level == 3:  # 3번 이동 완료
        if prey_count > max_prey[0]:  # 더 많은 몬스터를 잡았다면 갱신
            max_prey = [prey_count, r, c, path[:]]  # (사냥 수, 최종 위치, 이동 경로)
        return  # 종료

    for i in range(4):  # 상하좌우 이동 시도
        nr, nc = r + dr[i], c + dc[i]  # 다음 위치 계산
        if nr < 0 or nr > 3 or nc < 0 or nc > 3:  # 격자 범위 밖이면 continue
            continue
        elif (nr, nc) in path:  # 이미 지나온 경로면 continue
            packman_move(level + 1, prey_count, path, nr, nc)  # 다음 이동 탐색
        elif (nr, nc) not in path:  # 새로운 위치라면
            if (nr, nc) in new_monsters:  # 몬스터가 있다면
                packman_move(level + 1, prey_count + len(new_monsters[(nr, nc)]), path + [(nr, nc)], nr, nc)  # 사냥 수 증가
            else:  # 몬스터가 없다면
                packman_move(level + 1, prey_count, path + [(nr, nc)], nr, nc)  # 사냥 수 유지

# 격자 범위 확인 함수
def in_range(r, c):
    return -1 < r < 4 and -1 < c < 4

# 시뮬레이션 진행 (T턴 동안)
for time in range(T):
    new_monsters = {}  # 이동 후 몬스터 정보를 저장할 딕셔너리

    # 몬스터 이동 처리
    for r, c in monsters:  # 모든 몬스터 위치에 대해
        for d in monsters[(r, c)]:  # 각 몬스터의 방향에 대해
            for _ in range(8):  # 최대 8번 방향 전환 시도
                nr, nc = r + dr2[d], c + dc2[d]  # 이동 시도
                if not in_range(nr, nc) or (nr, nc) in smells or (nr, nc) == (R, C):  # 이동 불가능하면 방향 전환
                    d = (d + 1) % 8
                else:  # 이동 가능하면 break
                    break
            else:  # 8번 모두 이동 불가능하면 제자리에 멈춤
                nr, nc = r, c

            if (nr, nc) in new_monsters:  # 이미 다른 몬스터가 이동한 위치라면
                new_monsters[(nr, nc)].append(d)  # 방향 추가
            else:  # 새로운 위치라면
                new_monsters[(nr, nc)] = [d]  # 리스트 생성

    # 팩맨 이동 처리 (최대 사냥)
    max_prey = [-1, -1, -1, []]  # 초기값 설정
    packman_move(0, 0, [], R, C)  # DFS 탐색 시작

    # 팩맨이 몬스터를 잡아먹은 결과 반영
    for r, c in max_prey[3]:  # 팩맨 이동 경로에 대해
        if (r, c) in new_monsters:  # 몬스터가 있다면
            del new_monsters[(r, c)]  # 몬스터 제거
            smells[(r, c)] = 3  # 냄새 생성 (3턴 지속)

    R, C = max_prey[1], max_prey[2]  # 팩맨 위치 업데이트

    # 냄새 감소 및 소멸 처리
    expired_smells = []  # 소멸될 냄새 위치 저장
    for r, c in smells:  # 모든 냄새 위치에 대해
        smells[(r, c)] -= 1  # 냄새 턴 감소
        if smells[(r, c)] == 0:  # 냄새 소멸
            expired_smells.append((r, c))

    for r, c in expired_smells:  # 소멸될 냄새 제거
        del smells[(r, c)]

    # 새로운 몬스터 정보 갱신
    for r, c in new_monsters:  # 모든 몬스터 위치에 대해
        if (r, c) in monsters:  # 기존 몬스터가 있는 위치라면
            monsters[(r, c)].extend(new_monsters[(r, c)])  # 방향 추가
        else:  # 새로운 위치라면
            monsters[(r, c)] = new_monsters[(r, c)][:]  # 복사

# 결과 출력
answer = sum(len(monsters[(r, c)]) for r, c in monsters)  # 모든 몬스터 수 합
print(answer)