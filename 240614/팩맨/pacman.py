dr=[-1,0,1,0]
dc=[0,-1,0,1]
dr2=[-1,-1,0,1,1,1,0,-1]
dc2=[0,-1,-1,-1,0,1,1,1]

# 입력 받기
M, T = map(int, input().split())
R, C = map(int, input().split())
R, C = R - 1, C - 1  # 팩맨 좌표 조정

# 몬스터와 시체정보 담을 딕셔너리 초기화
monsters = {}
dead_monsters = {}

# 몬스터 정보 입력 받기
for _ in range(M):
    r, c, d = map(int, input().split())
    pos = (r - 1, c - 1)
    if pos in monsters:
        monsters[pos].append(d - 1)
    else:
        monsters[pos] = [d - 1]

# 팩맨의 이동을 처리하는 함수
def packman_move(level, prey_count, path, r, c):
    global max_prey
    if level == 3:
        if prey_count > max_prey[0]:
            max_prey = [prey_count, r, c, path[:]]
        return
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr > 3 or nc < 0 or nc > 3:
            continue
        elif (nr, nc) in path:
            packman_move(level + 1, prey_count, path, nr, nc)
        elif (nr, nc) not in path:
            if (nr, nc) in new_monsters:
                packman_move(level + 1, prey_count + len(new_monsters[(nr, nc)]), path + [(nr, nc)], nr, nc)
            else:
                packman_move(level + 1, prey_count, path + [(nr, nc)], nr, nc)

def in_range(r,c):
    return -1<r<4 and -1<c<4

# 시뮬레이션 진행
for time in range(T):
    new_monsters = {}
    
    # 몬스터 이동
    for r, c in monsters:
        for d in monsters[(r, c)]:
            for _ in range(8):
                nr, nc = r + dr2[d], c + dc2[d]
                if not in_range(nr,nc) or (nr, nc) in dead_monsters or (nr, nc) == (R, C):
                    d = (d + 1) % 8 
                else:
                    break
            else:
                nr, nc = r, c
            
            if (nr, nc) in new_monsters:
                new_monsters[(nr, nc)].append(d)
            else:
                new_monsters[(nr, nc)] = [d]
    
    # 팩맨의 이동 및 최대 사냥 계산
    max_prey = [-1, -1, -1, []]
    packman_move(0, 0, [], R, C)
    
    # 팩맨의 사냥 결과 반영
    for r, c in max_prey[3]:
        if (r, c) in new_monsters:
            del new_monsters[(r, c)]
            dead_monsters[(r, c)] = 3
    
    R, C = max_prey[1], max_prey[2]

    # 시체 감소 및 소멸 처리
    expired_dead_monsters = []
    for r, c in dead_monsters:
        dead_monsters[(r, c)] -= 1
        if dead_monsters[(r, c)] == 0:
            expired_dead_monsters.append((r, c))
    
    for r, c in expired_dead_monsters:
        del dead_monsters[(r, c)]

    # 새로운 몬스터 정보 갱신
    for r, c in new_monsters:
        if (r, c) in monsters:
            monsters[(r, c)].extend(new_monsters[(r, c)])
        else:
            monsters[(r, c)] = new_monsters[(r, c)][:]

# 결과 출력
answer = sum(len(monsters[(r, c)]) for r, c in monsters)
print(answer)