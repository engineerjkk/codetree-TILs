import sys
input = sys.stdin.readline
N,M,P,C,D=map(int,input().split())

rudolf=list(map(int,input().split()))
rudolf[0]-=1
rudolf[1]-=1

santas=[[0]*2 for _ in range(P)]
for _ in range(P):
    n,r,c=map(int,input().split())
    santas[n-1][0]=r-1
    santas[n-1][1]=c-1

status=[0]*P
score=[0]*P

def rudolf_to_santa(sr,sc,rr,rc):
    r,c=0,0
    if sr-rr!=0:
        r=(sr-rr)//abs(sr-rr)
    if sc-rc!=0:
        c=(sc-rc)//abs(sc-rc)
    return r,c

def in_range(r,c):
    return -1<r<N and -1<c<N

def check_santa(r,c):
    for i in range(P):
        if santas[i][0]==r and santas[i][1]==c:
            return i
    return -1

def push_santa(i,rr,rc,C):
    if not in_range(santas[i][0]+rr*C,santas[i][1]+rc*C):
        santas[i][0]+=rr*C
        santas[i][1]+=rc*C
        status[i]=-1
    s=check_santa(santas[i][0]+rr*C,santas[i][1]+rc*C)
    if s!=-1:
        push_santa(s,rr,rc,1)
    santas[i][0]+=rr*C
    santas[i][1]+=rc*C
    return

def check_collision(rr,rc,C):
    for i in range(P):
        if santas[i][0]==rudolf[0] and santas[i][1]==rudolf[1]:
            push_santa(i,rr,rc,C) 
            score[i]+=C
            if status[i]!=-1:
                status[i]=2
            return

def move_rudolf():
    santa_info=[0,0,0,sys.maxsize]
    for i in range(P):
        if status[i]!=-1:
            distance=(santas[i][0]-rudolf[0])**2+(santas[i][1]-rudolf[1])**2
            if distance<santa_info[3]:
                santa_info=[i,santas[i][0],santas[i][1],distance]
            elif distance==santa_info[3]:
                if santa_info[1]<santas[i][0]:
                    santa_info=[i,santas[i][0],santas[i][1],distance]
                elif santa_info[1]==santas[i][0] and santa_info[2]<santas[i][1]:
                    santa_info=[i,santas[i][0],santas[i][1],distance]
    rr,rc=rudolf_to_santa(santa_info[1],santa_info[2],rudolf[0],rudolf[1])
    rudolf[0]+=rr
    rudolf[1]+=rc
    check_collision(rr,rc,C)
    return

def santa_to_rudolf(sr,sc,rr,rc):
    ret_r,ret_c=0,0
    distance=(sr-rr)**2+(sc-rc)**2
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    for i in range(4):
        nr=sr+dr[i]
        nc=sc+dc[i]
        if in_range(nr,nc) and check_santa(nr,nc)==-1:
            distance2=(nr-rr)**2+(nc-rc)**2
            if distance2<distance:
                distance=distance2
                ret_r=dr[i]
                ret_c=dc[i]
    return ret_r,ret_c

def move_santa(i):
    sr,sc=santa_to_rudolf(santas[i][0],santas[i][1],rudolf[0],rudolf[1])
    santas[i][0]+=sr
    santas[i][1]+=sc
    if santas[i][0]==rudolf[0] and santas[i][1]==rudolf[1]:
        score[i]+=D
        if status[i]!=-1:
            status[i]=2
        push_santa(i,-sr,-sc,D)
    return 

for _ in range(M):
    move_rudolf()
    for i in range(P):
        if status[i]==0:
            move_santa(i)
    for i in range(P):
        if status[i]!=-1:
            score[i]+=1
            status[i]=max(0,status[i]-1)
    for i in range(P):
        if status[i]!=-1:
            break
    else:
        break
print(*score)