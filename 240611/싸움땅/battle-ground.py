import sys
input = sys.stdin.readline
EMPTY=(-1,-1,-1,-1,-1,-1)
n,m,k=map(int,input().split())
gun=[[[] for _ in range(n)] for _ in range(n)]
print(gun)
for i in range(n):
    nums=list(map(int,input().split()))
    for j in range(n):
        if nums[j]!=0:
            gun[i][j].append(nums[j])

players=[]
for i in range(m):
    r,c,d,s=map(int,input().split())
    players.append((i,r-1,c-1,d,s,0))
dr=[-1,0,1,0]
dc=[0,1,0,-1]
points=[0]*m

def in_range(r,c):
    return -1<r<n and -1<c<n

def get_next(r,c,d):
    nr=r+dr[d]
    nc=c+dc[d]
    if not in_range(nr,nc):
        d=(d+2)%4
        nr=r+dr[d]
        nc=c+dc[d]
    return nr,nc,d

def find_player(pos):
    for i in range(m):
        _,r,c,_,_,_=players[i]
        if pos==(r,c):
            return players[i]
    return EMPTY

def update(p):
    num,_,_,_,_,_=p
    for i in range(m):
        num_i,_,_,_,_,_=players[i]
        if num_i==num:
            players[i]=p
            break
def move(p,pos):
    num,r,c,d,s,a=p
    nr,nc=pos
    gun[nr][nc].append(a)
    gun[nr][nc].sort(reverse=True)
    a=gun[nr][nc][0]
    gun[nr][nc].pop(0)
    p=(num,nr,nc,d,s,a)
    update(p)

def loser_move(p):
    num,r,c,d,s,a=p
    gun[r][c].append(a)
    for i in range(4):
        d=(d+i)%4
        nr=r+dr[d]
        nc=c+dc[d]
        if in_range(nr,nc) and find_player((nr,nc))==EMPTY:
            p=(num,r,c,d,s,0)
            move(p,(nr,nc))
            break
def fight(p1,p2,pos):
    num1,_,_,d1,s1,a1=p1
    num2,_,_,d2,s2,a2=p2
    if (s1+a1,s1)>(s2+a2,s2):
        points[num1]+=(s1+a1)-(s2+a2)
        loser_move(p2)
        move(p1,pos)
    else:
        points[num2]+=(s2+a2)-(s1+a1)
        loser_move(p1)
        move(p2,pos)

def simulate():
    for i in range(m):
        num,r,c,d,s,a=players[i]
        nr,nc,d=get_next(r,c,d)
        next_player=find_player((nr,nc))
        curr_player=(num,nr,nc,d,s,a)
        update(curr_player)
        if next_player==EMPTY:
            move(curr_player,(nr,nc))
        else:
            fight(curr_player,next_player,(nr,nc))

for _ in range(k):
    simulate()
print(*points)