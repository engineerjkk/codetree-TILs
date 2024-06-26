from collections import deque
MAX_N=31
MAX_L=41
dr=[-1,0,1,0]
dc=[0,1,0,-1]

info=[[0]*MAX_L for _ in range(MAX_L)]
bef_k=[0]*MAX_L
R=[0]*MAX_N
C=[0]*MAX_N
H=[0]*MAX_N
W=[0]*MAX_N
K=[0]*MAX_N
nr=[0]*MAX_N
nc=[0]*MAX_N
dmg=[0]*MAX_N
is_moved=[False]*MAX_N

def try_movement(idx,dir):
    queue=deque()
    is_pos=True
    for i in range(1,N+1):
        dmg[i]=0
        is_moved[i]=False
        nr[i]=R[i]
        nc[i]=C[i]
    queue.append(idx)
    is_moved[idx]=True
    while queue:
        r=queue.popleft()
        nr[r]+=dr[dir]
        nc[r]+=dc[dir]
        if nr[r]<1 or nc[r]<1 or nr[r]+H[r]-1>L or nc[r]+W[r]-1>L:
            return False

        for i in range(nr[r],nr[r]+H[r]):
            for j in range(nc[r],nc[r]+W[r]):
                if info[i][j]==1:
                    dmg[r]+=1
                if info[i][j]==2:
                    return False

        for i in range(1,N+1):
            if is_moved[i] or K[i]<=0:
                continue
            if R[i]>nr[r]+H[r]-1 or nr[r]>R[i]+H[i]-1:
                continue
            if C[i]>nc[r]+W[r]-1 or nc[r]>C[i]+W[i]-1:
                continue
            is_moved[i]=True
            queue.append(i)
    dmg[idx]=0
    return True

def move_piece(idx,move_dir):
    if K[idx]<=0:
        return
    if try_movement(idx,move_dir):
        for i in range(1,N+1):
            R[i]=nr[i]
            C[i]=nc[i]
            K[i]-=dmg[i]

L,N,Q=map(int,input().split())
for i in range(1,L+1):
    info[i][1:]=map(int,input().split())
for i in range(1,N+1):
    R[i],C[i],H[i],W[i],K[i]=map(int,input().split())
    bef_k[i]=K[i]

for _ in range(Q):
    idx,d=map(int,input().split())
    move_piece(idx,d)

ans=[]
for i in range(1,N+1):
    if K[i]>0:
        ans.append(bef_k[i]-K[i])
print(sum(ans))