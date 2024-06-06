import sys
input = sys.stdin.readline
from collections import deque
MAX_L=41
MAX_N=31
space=[[0]*MAX_L for _ in range(MAX_L)]
R=[0]*MAX_N
C=[0]*MAX_N
H=[0]*MAX_N
W=[0]*MAX_N
K=[0]*MAX_N
initial_K=[0]*MAX_N
nr=[0]*MAX_N
nc=[0]*MAX_N
dmg=[0]*MAX_N
is_moved=[False]*MAX_N
dr=[-1,0,1,0]
dc=[0,1,0,-1]

def try_movement(idx,d):
    for i in range(1,N+1):
        nr[i]=R[i]
        nc[i]=C[i]
        dmg[i]=0
        is_moved[i]=False
    queue=deque()
    queue.append(idx)
    is_moved[idx]=True
    while queue:
        r=queue.popleft()
        nr[r]+=dr[d]
        nc[r]+=dc[d]
        if nr[r]<1 or nc[r]<1 or nr[r]+H[r]-1>L or nc[r]+W[r]-1>L:
            return False
        
        for i in range(nr[r],nr[r]+H[r]):
            for j in range(nc[r],nc[r]+W[r]):
                if space[i][j]==1:
                    dmg[r]+=1
                if space[i][j]==2:
                    return False
        
        for i in range(1,N+1):
            if is_moved[i] or K[i]<=0:
                continue
            if R[i]>nr[r]+H[r]-1 or nr[r]>R[i]+H[i]-1:
                continue
            if C[r]>nc[r]+W[r]-1 or nc[r]>C[i]+W[i]-1:
                continue
            is_moved[i]=True
            queue.append(i)
    dmg[idx]=0
    return True
    

def move_piece(idx,d):
    if K[idx]<=0:
        return
    if try_movement(idx,d):
        for i in range(1,N+1):
            R[i]=nr[i]
            C[i]=nc[i]
            K[i]-=dmg[i]

L,N,Q=map(int,input().split())
for i in range(1,L+1):
    space[i][1:]=map(int,input().split())
for i in range(1,N+1):
    R[i],C[i],H[i],W[i],K[i]=map(int,input().split())
    initial_K[i]=K[i]
for _ in range(Q):
    idx,d=map(int,input().split())
    move_piece(idx,d)
ans=[]
for i in range(1,N+1):
    if K[i]>0:
        ans.append(initial_K[i]-K[i])
print(sum(ans))