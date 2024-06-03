from collections import deque
MAX=70
R,C,K=0,0,0
space=[[0]*MAX for _ in range(MAX+3)]
dr=[-1,0,1,0]
dc=[0,1,0,-1]
Exit=[[False]*MAX for _ in range(MAX+3)]
answer=0

def canGo(r,c):
    flag=-1<c-1 and c+1<C and -1<r-1 and r+1<R+3
    flag=flag and space[r][c-1]==0 and space[r][c+1]==0 and space[r][c]==0
    flag=flag and space[r+1][c]==0 and space[r-1][c]==0
    flag=flag and space[r-1][c-1]==0 and space[r-1][c+1]==0 
    return flag

def inRange(r,c):
    return 2<r<R+3 and -1<c<C

def resetSpace():
    for i in range(R+3):
        for j in range(C):
            space[i][j]=0
            Exit[i][j]=False

def bfs(r,c):
    result = r
    queue=deque()
    queue.append((r,c))
    visit=[[False]*C for _ in range(R+3)]
    visit[r][c]=True
    while queue:
        r,c=queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            #같은 방의 입구로가서 다른 방의 입구로 간다.
            if inRange(nr,nc) and not visit[nr][nc] and (space[nr][nc]==space[r][c] or (space[nr][nc]!=0 and Exit[r][c])):
                queue.append((nr,nc))
                visit[nr][nc]=True
                result=max(result,nr)
    return result

def down(r,c,d,id):
    if canGo(r+1,c):
        down(r+1,c,d,id)
    elif canGo(r+1,c-1):
        down(r+1,c-1,(d+3)%4,id)
    elif canGo(r+1,c+1):
        down(r+1,c+1,(d+1)%4,id)
    else:
        if not inRange(r-1,c-1) or not inRange(r-1,c+1):
            resetSpace()
        else:
            space[r][c]=id
            for i in range(4):
                nr=r+dr[i]
                nc=c+dc[i]
                space[nr][nc]=id
            Exit[r+dr[d]][c+dc[d]]=True
            global answer
            answer+=bfs(r,c)-3+1

R,C,K = map(int,input().split())
for id in range(1,K+1):
    c,d=map(int,input().split())
    down(0,c-1,d,id)
print(answer)