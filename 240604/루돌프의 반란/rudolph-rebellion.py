import sys
input = sys.stdin.readline
N,M,P,C,D=map(int,input().split())
rudolf=list(map(int,input().split()))
rudolf[0]-=1
rudolf[1]-=1
santas=[[0]*2 for _ in range(P)]
for _ in range(P):
    n,r,c=map(int,input().split())
    santas[n-1][0],santas[n-1][1]=r-1,c-1
score,status=[0]*P,[0]*P
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def santa_to_rudolf(r1,c1,r2,c2):
    distance=((r1-r2)**2)+((c1-c2)**2)
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

def move_santa(number):
    sr,sc=santa_to_rudolf(santas[number][0],santas[number][1],rudolf[0],rudolf[1])
    santas[number][0]+=sr
    santas[number][1]+=sc
    if santas[number][0]==rudolf[0] and santas[number][1]==rudolf[1]:
        push_santa(number,-sr,-sc,D)
        score[number]+=D
        if status[number]!=-1:
            status[number]=2
    return

def check_santa(r,c):
    for i in range(P):
        if r==santas[i][0] and c==santas[i][1]:
            return i
    return -1

def in_range(r,c):
    return -1<r<N and -1<c<N
def push_santa(number,cr,cc,power):
    if not in_range(santas[number][0]+cr*power,santas[number][1]+cc*power):
        santas[number][0]+=cr*power
        santas[number][1]+=cc*power
        status[number]=-1
        return
    s=check_santa(santas[number][0]+cr*power,santas[number][1]+cc*power)
    if s!=-1:
        push_santa(s,cr,cc,1)
    santas[number][0]+=cr*power
    santas[number][1]+=cc*power
    return


def check_collision(cr,cc,power):
    for i in range(P):
        if rudolf[0]==santas[i][0] and rudolf[1]==santas[i][1]:
            push_santa(i,cr,cc,power)
            score[i]+=power
            if status[i]!=-1:
                status[i]=2
            break
    return

def rudolf_to_santa(r1,c1,r2,c2):
    r,c=0,0
    if r2-r1!=0:
        r=(r2-r1)//abs(r2-r1)
    if c2-c1!=0:
        c=(c2-c1)//abs(c2-c1)
    return r,c
def move_rudolf():
    s_info=[0,0,0,sys.maxsize]
    for i in range(P):
        if status[i]!=-1:
            distance=(rudolf[0]-santas[i][0])**2 + (rudolf[1]-santas[i][1])**2
            if distance<s_info[3]:
                s_info=[i,santas[i][0],santas[i][1],distance]
            elif distance==s_info[3]:
                if s_info[1]<santas[i][0]:
                    s_info=[i,santas[i][0],santas[i][1],distance]
                elif s_info[1]==santas[i][0] and s_info[2]<santas[i][1]:
                    s_info=[i,santas[i][0],santas[i][1],distance]
    #가장 우선순위가 높은 산타를 향해 8방향 중 가장 가까워지는 방향으로 한칸 돌진
    move_r,move_c=rudolf_to_santa(rudolf[0],rudolf[1],s_info[1],s_info[2])
    rudolf[0]+=move_r
    rudolf[1]+=move_c
    check_collision(move_r,move_c,C)
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