sharkdir = [(-1,0),(0,-1),(1,0),(0,1)]  # 상좌하우
dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
M, T = map(int, input().split())
R, C = map(int, input().split())
R, C = R-1, C-1  # 팩맨 좌표
monster = {}
smell = {}
for _ in range(M):
    a, b, c = map(int, input().split())
    if (a-1,b-1) in monster: monster[(a-1,b-1)].append(c-1)
    else: monster[(a-1,b-1)] = [c-1]

def packmove(level,cnt,llist,x,y):
    global maxprey
    if level==3:
        if cnt>maxprey[0]:
            maxprey = [cnt,x,y,llist[:]]
        return
    for i in range(4):
        nx, ny = x+sharkdir[i][0], y+sharkdir[i][1]
        if nx<0 or nx>3 or ny<0 or ny>3: continue
        elif (nx,ny) in llist:
            packmove(level+1,cnt,llist,nx,ny)
        elif (nx,ny) not in llist:
            if (nx,ny) in new_monster: packmove(level+1,cnt+len(new_monster[(nx,ny)]),llist+[(nx,ny)],nx,ny)
            else: packmove(level+1,cnt,llist+[(nx,ny)],nx,ny)

for time in range(T):
    new_monster = {}
    for x,y in monster:
        for d in monster[(x,y)]:
            for _ in range(8):
                nx, ny = x+dir[d][0], y+dir[d][1]
                if 0>nx or 3<nx or 0>ny or 3<ny or (nx,ny) in smell or (nx,ny)==(R,C):
                    d = (d+1)%8
                else: break
            else: nx, ny = x, y
            if (nx,ny) in new_monster: new_monster[(nx,ny)].append(d)
            else: new_monster[(nx,ny)] = [d]  # 0:북 2:서 4:남 6:동

    maxprey = [-1,-1,-1,[]]  # 수, 좌표
    packmove(0,0,[],R,C)
    for x,y in maxprey[3]:

        if (x,y) in new_monster:
            del new_monster[(x,y)]
            smell[(x,y)] = 3
    R, C = maxprey[1], maxprey[2]

    llist = []
    for x,y in smell:
        smell[(x,y)] -= 1
        if smell[(x,y)] == 0:
            llist.append((x,y))
    for x,y in llist:  # 0이 된 냄새 소멸
        del smell[(x,y)]

    for x,y in new_monster:
        if (x,y) in monster:
            monster[(x,y)].extend(new_monster[(x,y)])
        else:
            monster[(x,y)] = new_monster[(x,y)][:]

answer = 0
for x,y in monster:
    answer += len(monster[(x,y)])
print(answer)