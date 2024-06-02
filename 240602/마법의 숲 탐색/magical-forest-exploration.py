from collections import deque
MAX_L=70
R,C,K=0,0,0
A=[[0]*MAX_L for _ in range(MAX_L+3)]
dr=[-1,0,1,0]
dc=[0,1,0,-1]
isExit=[[False]*MAX_L for _ in range(MAX_L+3)]
answer=0

def canGo(r,c):
    #한 칸 내려갔을 때
    #중심점이 범위에 있어야한다.
    flag= -1<c-1 and c+1<C and -1<r-1 and r+1<R+3
    #내려갔을 때 양 옆에 공간이 있어야한다.
    flag = flag and A[r][c-1]==0 and A[r][c+1]==0
    # 한칸 더 아래도 체크해야한다.
    flag = flag and A[r+1][c]==0 and A[r-1][c]==0
    # 내려가기 전에도 양 옆을 체크해야한다.
    flag = flag and A[r-1][c-1]==0 and A[r-1][c+1]==0
    return flag

def inRange(r,c):
    return 2<r<R+3 and -1<c<C

def resetMap():
    for i in range(R+3):
        for j in range(C):
            A[i][j]=0
            isExit[i][j]=False

def bfs(r,c):
    result=r
    queue=deque()
    queue.append((r,c))
    visit=[[False]*C for _ in range(R+3)]
    visit[r][c]=True
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if inRange(nr,nc) and not visit[nr][nc] and (A[nr][nc]==A[r][c] or (A[nr][nc]!=0 and isExit[r][c])): 
                queue.append((nr,nc))
                visit[nr][nc]=True
                result=max(result,nr)
    return result


# 0,1,2,3은 북,동,남,서
def down(r,c,d,id):
    #일단 우선 아래로 내려간다.
    if canGo(r+1,c):
        down(r+1,c,d,id)
    #아래로 못내려가면 서쪽으로 내려간다.
    elif canGo(r+1,c-1):
        down(r+1,c-1,(d+3)%4,id)
    #왼쪽으로 못내려가면 동쪽으로 내려간다.
    elif canGo(r+1,c+1):
        down(r+1,c+1,(d+1)%4,id)
    #다 내려갔으면 정착한다.
    else:
        #숲의 범위를 벗어나면 모든 골렘이 숲을 빠져나간다.
        #r과 c는 중심 점을 나타낸다.
        if not inRange(r-1,c-1) or not inRange(r-1,c+1):
            resetMap()
        else:
            A[r][c]=id
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                A[nr][nc]=id
            #골렘의 출구를 기록한다.
            isExit[r+dr[d]][c+dc[d]]=True
            global answer
            answer+=bfs(r,c)-3+1
        


R,C,K=map(int,input().split())
for id in range(1,K+1):
    c,d=map(int,input().split())
    down(0,c-1,d,id)
print(answer)