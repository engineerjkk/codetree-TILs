import sys
input = sys.stdin.readline

n,m=map(int,input().split())
r,c,d=map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
visit=[[False]*m for _ in range(n)]
visit[r][c]=True
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def simulate():
    global r,c,d
    visit[r][c]=True
    for _ in range(4):
        d=(d-1+4)%4
        nr=r+dr[d]
        nc=c+dc[d]
        if space[nr][nc]==0 and not visit[nr][nc]:
            r,c=nr,nc
            return True
    br=r-dr[d]
    bc=c-dc[d]
    if space[br][bc]==0:
        r,c=br,bc
        return True
    else:
        return False

while True:
    if not simulate():
        break

ans=0
for i in range(n):
    for j in range(m):
        if visit[i][j]==True:
            ans+=1
print(ans)