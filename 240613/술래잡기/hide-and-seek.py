import sys
input = sys.stdin.readline

n,m,h,k=map(int,input().split())
change_direction=[(0,0),(n//2,n//2)]
runner_dict={}
runner_map=[[[] for _ in range(n)] for _ in range(n)]
tree_map=[[0]*n for _ in range(n)]
score=0

class Runner:
    def __init__(self,id,r,c,d):
        self.id=id
        self.r=r
        self.c=c
        self.d=d
    def get_next(self):
        return self.r+self.d[0],self.c+self.d[1]
    def change_dir(self):
        self.d=(self.d[0]*-1,self.d[1]*-1)

class Catcher:
    def __init__(self,r,c,d):
        self.r=r
        self.c=c
        self.d=d
        self.flag=True
    def move(self):
        self.r+=self.d[0]
        self.c+=self.d[1]
        return self.r,self.c


for i in range(n//2):
    change_direction.append((max(n//2-i-1,0),n//2-i))
    change_direction.append((n//2-i-1,n//2+i+1))
    change_direction.append((n//2-i-1,n//2+i+1))
    change_direction.append((n//2-i-1,n//2+i+1))

for i in range(m):
    r,c,d=map(int,input().split())
    if d==1:
        d=(0,1)
    else:
        d=(1,0)
    runner_dict[i+1]=Runner(i+1,r-1,c-1,d)
    runner_map[r-1][c-1].append(i+1)

for _ in range(h):
    r,c=map(int,input().split())
    tree_map[r-1][c-1]=-1
catcher=Catcher(n//2,n//2,(-1,0))

def move_runner():
    for rid,runner in runner_dict.items():
        if abs(catcher.r-runner.r)+abs(catcher.c-runner.c)<=3:
            next_r,next_c=runner.get_next()
            if not(0<=next_r<n and 0<=next_c<n):
                runner.change_dir()
                next_r,next_c=runner.get_next()
            if (next_r,next_c) !=(catcher.r,catcher.c):
                runner_map[runner.r][runner.c].remove(runner.id)
                runner.r,runner.c=next_r,next_c
                runner_map[runner.r][runner.c].append(runner.id)
def move_catcher():
    a,b=catcher.r,catcher.c
    r,c=catcher.move()
    if (r,c) in change_direction:
        if r<n//2:
            if c>n//2:
                if catcher.flag:
                    catcher.d=(1,0)
                else:
                    catcher.d=(0,-1)
            else:
                if catcher.flag:
                    catcher.d=(0,1)
                else:
                    catcher.d=(1,0)
        else:
            if c>=n//2:
                if catcher.flag:
                    catcher.d=(0,-1)
                else:
                    catcher.d=(-1,0)
            else:
                if catcher.flag:
                    catcher.d=(-1,0)
                else:
                    catcher.d=(0,1)

def catch(t,score):
    r,c=catcher.r,catcher.c
    catch_runner=[]
    for i in range(3):
        watch_r,watch_c=r+catcher.d[0]*i,c+catcher.d[1]*i
        if tree_map[watch_r][watch_c]==0 and runner_map[watch_r][watch_c]:
            runner_id_list=runner_map[watch_r][watch_c]
            for runner_id in runner_id_list:
                catch_runner.append(runner_dict[runner_id])
    for runner in catch_runner:
        runner_map[runner.r][runner.c].remove(runner.id)
        del runner_dict[runner.id]
    return score+len(catch_runner)*t
def rotate():
    if catcher.r==0 and catcher.c==0:
        catcher.d=(1,0)
        catcher.flag=False
    if catcher.r==n//2 and catcher.c==n//2:
        catcher.d=(-1,0)
        catcher.flag=True

t=1
score=0
while runner_dict and t<=k:
    move_runner()
    move_catcher()
    score=catch(t,score)
    rotate()
    t+=1
print(score)