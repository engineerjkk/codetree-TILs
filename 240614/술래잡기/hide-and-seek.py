import sys
input = sys.stdin.readline
n,m,h,k=map(int,input().split())
change_dir=[(n//2,n//2)]
for i in range(n//2):
    left_top=(n//2-i-1,n//2-i)
    right_top=(n//2-i-1,n//2+i+1)
    right_bottom=(n//2+i+1,n//2+i+1)
    left_bottom=(n//2+i+1,n//2-i-1)

    change_dir.append(left_top)
    change_dir.append(right_top)
    change_dir.append(right_bottom)
    change_dir.append(left_bottom)
change_dir.append((0,0))

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
        self.r=self.r+dr[d]
        self.c=self.c+dc[d]
        return self.r,self.c

runner_dic={}
runner_map=[[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    r,c,d=map(int,input().split())
    if d==1:
        d=1
    else:
        d=2
    runner_dic[i+1]=Runner(i+1,r-1,c-1,d)
    runner_map[r-1][c-1].append(i+1)

tree_map=[[0]*n for _ in range(n)]
for _ in range(h):
    r,c=map(int,input().split())
    tree_map[r-1][c-1]=-1

catcher=Catcher(n//2,n//2,0)

def in_range(r,c):
    return -1<r<n and -1<c<n

def move_runner():
    for key,runner in runner_dic.items():
        if abs(catcher.r-runner.r)+abs(catcher.c-runner.c)<=3:
            nr,nc=runner.get_next()
            if not in_range(nr,nc):
                runner.change_dir()
                nr,nc=runner.get_next()
            if (catcher.r,catcher.c)!=(nr,nc):
                runner_map[runner.r][runner.c].remove(runner.id)
                runner.r,runner.c=nr,nc
                runner_map[runner.r][runner.c].append(runner.id)#오타..

def move_catcher():
    r,c=catcher.move()
    if (r,c) in change_dir:
        if catcher.flag:
            if r<n//2:
                if c<=n//2:
                    catcher.d=1
                else:
                    catcher.d=2
            else:
                if c<=n//2:
                    catcher.d=0
                else:
                    catcher.d=3
        else:
            if r<n//2:
                if c<=n//2:
                    catcher.d=2
                else:
                    catcher.d=3
            else:
                if c<=n//2:
                    catcher.d=1
                else:
                    catcher.d=0

def catch(t):
    r,c=catcher.r,catcher.c
    caught_runner=[]
    for i in range(3):
        wr,wc=r+dr[catcher.d]*i,c+dc[catcher.d]*i
        if in_range(wr,wc):
            if tree_map[wr][wc]==0 and runner_map[wr][wc]:
                for runner_id in runner_map[wr][wc]:
                    caught_runner.append(runner_dic[runner_id])
    for runner in caught_runner:
        runner_map[runner.r][runner.c].remove(runner.id)
        del runner_dic[runner.id]
    return len(caught_runner)*t

def rotate():
    r,c=catcher.r,catcher.c
    if (r,c)==(0,0):
        catcher.d=2
        catcher.flag=False
    if (r,c)==(n//2,n//2):
        catcher.d=0
        catcher.flag=True


score=0
for t in range(1,k+1):
    if len(runner_dic)==0:
        break
    move_runner()
    move_catcher()
    score+=catch(t)
    rotate()
print(score)