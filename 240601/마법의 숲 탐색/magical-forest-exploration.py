from collections import deque
MAX_L = 70
R, C, K = 0,0,0
# 실제 숲을 [3~R+2][0~C-1]로 사용하기위해 행은 3만큼의 크기를 더 갖습니다
A=[[0]*MAX_L for _ in range(MAX_L+3)]
dy=[-1,0,1,0]
dx=[0,1,0,-1]
# g해당 칸이 골렘의 출구인지 저장한다.
isExit=[[False]*MAX_L for _ in range(MAX_L +3)]
answer=0

#골렘의 중심이 y,x에 위치할 수 있는지 확인한다.
#북쪽에서 남쪽으로 내려와야하므로 중심이 (y,x)에 위치할때의 범위와
#(y-1,x)에 위치할 때의 범위를 모두 확인한다.
def canGo(y,x):
    flag = 0<=x-1 and x+1 <C and y+1 < R+3
    flag = flag and (A[y-1][x-1]==0) # 왼쪽 아래에 공간이 있는경우
    flag = flag and (A[y-1][x]==0) #아래에 공간이있는경우
    flag = flag and (A[y-1][x+1]==0) #오른쪽 아래에 공간이 있는 경우
    flag = flag and (A[y][x-1]==0) #왼쪽에 공간이있는경우
    flag = flag and (A[y][x+1]==0) #오른쪽에 공간이 있는경우
    flag = flag and (A[y+1][x]==0) #위쪽에 공간이 있는경우
    return flag

# (y,x)가 숲의 범위 안에 있는지 확인하는 함수
def inRange(y,x):
    return 3<=y<R+3 and 0<=x<C

# 숲에 있는 골렘들이 모두 빠져나갑니다.
def resetMap():
    for i in range(R+3):
        for j in range(C):
            A[i][j]=0
            isExit[i][j]=False

#정령이 움직일 수 있는 모든 범위를 확인하고 도달할 수 있는 최하단 행을 반환한다. 
def bfs(y,x):
    result=y
    q=deque([(y,x)])
    visit=[[False]*C for _ in range(R+3)]
    visit[y][x]=True
    while q:
        cur_y,cur_x=q.popleft()
        for k in range(4):
            ny,nx=cur_y+dy[k],cur_x+dx[k]
            #정령의 움직임은 골렘 내부이거나
            #골렘의 탈출구에 위치하고 있다면 다른 골렘으로 옮겨 갈 수 있습니다.
            # 같은 방안에있거나, 빈곳이아니면서 탈출구여야한다.
            #범위 안에있고, 방문을 안했으며, 같은 index에있어야하며 
            if inRange(ny,nx) and not visit[ny][nx] and (A[ny][nx]==A[cur_y][cur_x] or (A[ny][nx]!=0 and isExit[cur_y][cur_x])):
                q.append((ny,nx))
                visit[ny][nx]=True
                result=max(result,ny)
    return result

def down(y,x,d,id):
    #아래로 내려갈 수 있는 경우
    if canGo(y+1,x):
        down(y+1,x,d,id)
    #왼쪽 아래로 내려갈 수 있는 경우
    elif canGo(y+1,x-1):
        down(y+1,x-1,(d+3)%4,id)
    #오른쪽 아래로 내려갈 수 있는 경우
    elif canGo(y+1,x+1):
        down(y+1,x+1,(d+1)%4,id)
    # 1,2,3의 움직임을 모두 취할 수 없을 때
    else:
        if not inRange(y-1,x-1) or not inRange(y+1,x+1):
            #숲을 벗어나는 경우 모든 골렘이 숲을 빠져나갑니다.
            resetMap()
        else:
            #골렘이 숲 안에 정착합니다.
            A[y][x]=id
            for k in range(4):
                A[y+dy[k]][x+dx[k]]=id
            #골렘의 출구를 기럭
            isExit[y+dy[d]][x+dx[d]]=True
            global answer
            #bfs를 통해 점령이 최대로 내려갈 수 있는 행을 계산하여 누적한다. 
            answer+=bfs(y,x)-3+1


#main
R,C,K = map(int,input().split())
for id in range(1,K+1): #골렘 번호 id
    #골렘의 출발 x좌표, 방향 d를 입력받는다.
    x,d=map(int,input().split())
    #가장 위부터이므로, y=0부터 시작한다. 1부터 시작하므로 x-1을 해준다. 
    down(0,x-1,d,id)
print(answer)