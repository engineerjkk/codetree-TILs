dir = [(-1,0),(0,1),(1,0),(0,-1)]  # 북동남서
N, M, H, K = map(int, input().split())
runner = {}
for _ in range(M):
    a, b, c = map(int, input().split())
    runner[(a-1,b-1)] = [c]
tree = set()
for _ in range(H):
    a, b = map(int, input().split())
    tree.add((a-1,b-1))
x, y = N//2, N//2

d = 0
turncnt = 0
distance = 1
dist = 0
llist = [(N//2,N//2,0)]  # 맨 처음인데 이거는 처음에는 봐줄 일 없으니
# 인덱스를 1부터 시작인걸로 하자. len으로 나눈 나머지로 인덱스 하면 되겠다 ㅎㅎ
while True:
    x, y = x+dir[d][0], y+dir[d][1]
    dist += 1
    if (x,y) == (0,0):
        llist.append((0,0,2))
        break
    if dist == distance:
        dist = 0
        d = (d+1)%4
        turncnt += 1
        if turncnt == 2:
            turncnt = 0
            distance += 1
    llist.append((x, y, d))

d = 2
turncnt = 1
dist = 1
while True:
    x, y = x+dir[d][0], y+dir[d][1]
    dist += 1
    if (x,y) == (N//2,N//2):
        break
    if dist == distance:
        dist = 0
        d = (d-1)%4
        turncnt += 1
        if turncnt == 2:
            turncnt = 0
            distance -= 1
    llist.append((x,y,d))

# =========== 여기서부터 턴 시작 llist이용, index는 1부터
score = 0
for time in range(1,K+1):
    bt = (time-1)%((N**2-1)*2)
    at = time%((N**2-1)*2)
    delrunlist = []
    runlist = []
    for x,y in runner:
        if abs(x-llist[bt][0])+abs(y-llist[bt][1])<4:
            delrunlist.append((x,y))
            for d in runner[(x,y)]:
                run = d
                nx, ny = x+dir[run][0], y+dir[run][1]
                if 0>nx or N-1<nx or 0>ny or N-1<ny:
                    run = (run+2)%4
                    nx, ny = x+dir[run][0], y+dir[run][1]
                if (nx,ny) != (llist[bt][0],llist[bt][1]):
                    runlist.append((nx,ny,run))
                else:
                    runlist.append((x,y,run))

    for x,y in delrunlist:
        del runner[(x,y)]
    for new in runlist:
        if (new[0],new[1]) in runner:
            runner[(new[0],new[1])].append(new[2])
        else:
            runner[(new[0],new[1])] = [new[2]]
    # 여기까지 도망자들 이동

    x,y,d = llist[at]
    for j in range(3):
        nx, ny = x+dir[d][0]*j,y+dir[d][1]*j
        if (nx,ny) in runner and (nx,ny) not in tree:
            score += len(runner[(nx,ny)])*time
            del runner[(nx,ny)]
print(score)