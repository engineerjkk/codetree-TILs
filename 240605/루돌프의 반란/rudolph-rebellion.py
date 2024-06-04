import sys
input = sys.stdin.readline
N,M,P,C,D = map(int,input().split())
rudolf=list(map(int,input().split()))
rudolf[0]-=1
rudolf[1]-=1
santas=[[0]*2 for _ in range(P)]
for _ in range(P):
    n,r,c=map(int,input().split())
    santas[n-1][0]=r-1
    santas[n-1][1]=c-1

score=[0]*P
status=[0]*P
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def check_santa(r,c):
    for i in range(P):
        if santas[i][0]==r and santas[i][1]==c:
            return i
    return -1

def in_range(r,c):
    return -1<r<N and -1<c<N

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
        if rudolf[0]==santas[i][0] and rudolf[1]==santas[i][1]:
            push_santa(i,rr,rc,C)
            score[i]+=C
            if status[i]!=-1:
                status[i]=2
            break
    return

def rudolf_to_santa(r1,r2,c1,c2):
    r,c=0,0
    if r2-r1!=0:
        r=(r2-r1)//abs(r2-r1)
    if c2-c1!=0:
        c=(c2-c1)//abs(c2-c1)
    return r,c


def move_rudolf():
    santa_info=[0,0,0,sys.maxsize]
    for i in range(P):
        if status[i]!=-1:
            distance=(rudolf[0]-santas[i][0])**2+(rudolf[1]-santas[i][1])**2
            if distance<santa_info[3]:
                santa_info=[i,santas[i][0],santas[i][1],distance]
            elif distance==santa_info[3]:
                if santa_info[1]<santas[i][0]:
                    santa_info=[i,santas[i][0],santas[i][1],distance]
                elif santa_info[1]==santas[i][0] and santa_info[2]<santas[i][1]:
                    santa_info=[i,santas[i][0],santas[i][1],distance]
    rr,rc=rudolf_to_santa(rudolf[0],santa_info[1],rudolf[1],santa_info[2])
    rudolf[0]+=rr
    rudolf[1]+=rc
    check_collision(rr,rc,C)
    return

def santa_to_rudolf(r1,c1,r2,c2):
    distance=((r1-r2)**2) +((c1-c2)**2)
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    ret_r=0
    ret_c=0
    for i in range(4):
        nr=r1+dr[i]
        nc=c1+dc[i]
        if in_range(nr,nc) and check_santa(nr,nc)==-1:
            distance2=((nr-r2)**2)+((nc-c2)**2)
            if distance2<distance:
                ret_r=dr[i]
                ret_c=dc[i]
                distance=distance2
    return ret_r,ret_c


def move_santa(i):
    sr,sc=santa_to_rudolf(santas[i][0],santas[i][1],rudolf[0],rudolf[1])
    santas[i][0]+=sr
    santas[i][1]+=sc
    if santas[i][0]==rudolf[0] and santas[i][1]==rudolf[1]:
        push_santa(i,-sr,-sc,D)
        score[i]+=D
        if status[i]!=-1:
            status[i]=2
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
    lst=[]
    for i in range(P):
        if status[i]==-1:
            lst.append(True)
        else:
            lst.append(False)
    if all(lst):
        break
    else:
        continue
print(*score)