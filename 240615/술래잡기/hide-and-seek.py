import sys
input = sys.stdin.readline
from collections import deque
N,M,H,K=map(int,input().split())

catcher_dir=[(N//2,N//2)]
for i in range(N//2):
    left_top=(N//2-i-1,N//2-i)
    right_top=(N//2-i-1,N//2+i+1)
    right_bottom=(N//2+i+1,N//2+i+1)
    left_bottom=(N//2+i+1,N//2-i-1)

    catcher_dir.append(left_top)
    catcher_dir.append(right_top)
    catcher_dir.append(right_bottom)
    catcher_dir.append(left_bottom)
catcher_dir.append((0,0))

dr=[-1,0,1,0]
dc=[0,1,0,-1]

class Runner:
    def __init__(self,id,r,c,d):
        self.id=id
        self.r=r
        self.c=c
        self.d=d
    def get_next(self):
        return self.r+dr[self.d],self.c+dc[self.d]
    def change_dir(self):
        self.d=(self.d+2)%4

class Catcher:
    def __init__(self,r,c,d):
        self.r=r
        self.c=c
        self.d=d
        self.flag=True
    def move(self):
        self.r+=dr[self.d]
        self.c+=dc[self.d]
        return self.r,self.c

runner_dic={}
runner_map=[[[] for _ in range(N)] for _ in range(N)]
for i in range(M):
    r,c,d=map(int,input().split())
    if d==1:
        d=1
    else:
        d=2
    runner_dic[i+1]=Runner(i+1,r-1,c-1,d)
    runner_map[r-1][c-1].append(i+1)
tree_map=[[0]*N for _ in range(N)]
for _ in range(H):
    r,c=map(int,input().split())
    tree_map[r-1][c-1]=-1

catcher=Catcher(N//2,N//2,0)

def in_range(r,c):
    return -1<r<N and -1<c<N

def move_runners():
    for key,runner in runner_dic.items():
        if abs(runner.r-catcher.r)+abs(runner.c-catcher.c)<=3:
            nr,nc=runner.get_next()
            if not in_range(nr,nc):
                runner.change_dir()
                nr,nc=runner.get_next()
            if (nr,nc)!=(catcher.r,catcher.c):
                runner_map[runner.r][runner.c].remove(runner.id)
                runner.r,runner.c=nr,nc
                runner_map[runner.r][runner.c].append(runner.id)
def move_catcher():
    r,c=catcher.move()
    if (r,c) in catcher_dir:
        if catcher.flag:
            if r<N//2:
                if c<=N//2:
                    catcher.d=1
                else:
                    catcher.d=2
            else:
                if c<=N//2:
                    catcher.d=0
                else:
                    catcher.d=3
        else:
            if r<N//2:
                if c<=N//2:
                    catcher.d=2
                else:
                    catcher.d=3
            else:
                if c<=N//2:
                    catcher.d=1
                else:
                    catcher.d=0

def catch(t):
    r,c=catcher.r,catcher.c
    caught_runner=[]
    for i in range(3):
        wr,wc=r+dr[catcher.d]*i,c+dc[catcher.d]*i
        if tree_map[wr][wc]==0 and runner_map[wr][wc]:
            for runner_id in runner_map[wr][wc]:
                caught_runner.append(runner_dic[runner_id])
    for runner in caught_runner:
        runner_map[runner.r][runner.c].remove(runner.id)
        del runner_dic[runner.id]
    return len(caught_runner)*t

def rotate():
    r,c=catcher.r,catcher.c
    if (r,c)==(N//2,N//2):
        catcher.d=0
        catcher.flag=True
    if (r,c)==(0,0):
        catcher.d=2
        catcher.flag=False

score=0
for t in range(1,K+1):
    move_runners()
    move_catcher()
    score+=catch(t)
    rotate()
print(score)