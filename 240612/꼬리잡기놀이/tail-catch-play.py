from collections import deque
dir = [(1,0),(-1,0),(0,1),(0,-1)]

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _  in range(N)]
q = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            w = deque([(i,j)])
            e = deque([(i,j)])  # 점수는 인덱스로 계산하기!
            while w:
                x,y = w.popleft()
                for k in range(4):
                    nx, ny = x+dir[k][0], y+dir[k][1]

                    if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 2 and (nx,ny) not in e:
                        e.append((nx,ny))
                        w.append((nx,ny))
            x,y = e[-1][0], e[-1][1]
            for k in range(4):
                nx, ny = x+dir[k][0], y+dir[k][1]
                if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 3:
                    e.append((nx,ny))
                    break
            q.append(e)
# q에는 순서대로 헤드부터 테일까지의 기차들이 들어있다.

def move():
    for train in q:
        x,y = train.pop()  # tail
        graph[x][y] = 4    # 원래 선로로 돌려놓기
        graph[train[-1][0]][train[-1][1]] = 3 # 새로운 꼬리

        x,y = train[0]
        graph[x][y] = 2    # 원래 머리 위치는 몸통으로 만들기
        for i in range(4):
            nx, ny = x+dir[i][0], y+dir[i][1]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 4:
                graph[nx][ny] = 1
                train.appendleft((nx,ny))
                break

def ball(round):  # return은 (-1,-1) 즉 좌표로 해서, 큐에 접근하여 뒤바꿀 기차와 점수 알아내기
    round %= 4*N  # 이것때문에, 문제에서는 라운드1부터이지만 나는 0부터 4N-1까지 할거다.
    if round<N:  # 첫번째
        for j in range(N):
            if graph[round][j] in (1,2,3): return (round,j)
    elif round<2*N:
        for i in range(N):
            if graph[N-1-i][round-N] in (1,2,3): return (N-1-i,round-N)
    elif round<3*N:
        for j in range(N):
            if graph[3*N-1-round][N-1-j] in (1,2,3): return (3*N-1-round,N-1-j)
    else:
        for i in range(N):
            if graph[i][4*N-1-round] in (1,2,3): return(i,4*N-1-round)
    return (-1,-1)

def change(x,y):  # 점수를 리턴함
    if (x,y) == (-1,-1): return 0
    # (-1,-1) 아닐때만 작동시킴에 유의!
    for i in range(M):
        if (x,y) in q[i]:
            for j in range(len(q[i])):
                if q[i][j] == (x,y):
                    graph[q[i][0][0]][q[i][0][1]] = 3
                    graph[q[i][-1][0]][q[i][-1][1]] = 1
                    q[i].reverse()
                    return (j+1)**2

cnt = 0
for i in range(K):
    move()
    a,b = ball(i)
    cnt += change(a,b)
print(cnt)