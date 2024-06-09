import sys
input = sys.stdin.readline
from collections import deque


class Person():
    def __init__(self,r,c):
        self.r=r
        self.c=c

class Cu():
    def __init__(self,r,c):
        self.r=r
        self.c=c

class Candidate():
    def __init__(self,d,r,c):
        self.d=d
        self.r=r
        self.c=c

N,M = map(int,input().split())
space=[]
for _ in range(N):
    space.append(list(map(int,input().split())))

people=[]
cu=[]
for _ in range(M):
    r,c=map(int,input().split())
    cu.append(Cu(r-1,c-1))
    people.append(Person(-1,-1))

route=[[] for _ in range(M)]
dr=[-1,0,0,1]
dc=[0,-1,1,0]
time=0


def all_arrived():
    for i in range(M):
        if cu[i].r !=people[i].r or cu[i].c !=people[i].c:
            return False
    return True

def in_range(r,c):
    return -1<r<N and -1<c<N

def make_route(number,r,c):
    global route
    queue=deque()
    queue.append((r,c,[]))
    visited=[[False]*N for _ in range(N)]

    while queue:
        r,c,lst=queue.popleft()
        if r==cu[number].r and c==cu[number].c:
            route[number]=lst
            break
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and not visited[nr][nc] and space[nr][nc]!=-1:
                queue.append((nr,nc,lst+[(nr,nc)]))
                visited[nr][nc]=True
    return

def move_people():
    for i in range(M):
        r,c=people[i].r,people[i].c
        if (r==-1 and c==-1) or (r==cu[i].r and c==cu[i].c):
            continue
        if not route[i]:
            make_route(i,r,c)
        else:
            for rr,rc in route[i]:
                if space[rr][rc]==-1:
                    make_route(i,r,c)
                    break
        people[i].r=route[i][0][0]
        people[i].c=route[i][0][1]
        route[i]=route[i][1:]
    
    for i in range(M):
        r,c=people[i].r,people[i].c
        if r==-1 and c==-1:
            break
        if cu[i].r==r and cu[i].c==c:
            space[r][c]=-1
    return

def set_people(number):
    queue=deque()
    queue.append((cu[number].r,cu[number].c,0))
    visited=[[False]*N for _ in range(N)]
    candidate=[]
    while queue:
        r,c,d=queue.popleft()
        if space[r][c]==1:
            candidate.append(Candidate(d,r,c))
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if in_range(nr,nc) and not visited[nr][nc] and space[nr][nc]!=-1:
                queue.append((nr,nc,d+1))
                visited[nr][nc]=True
    candidate.sort(key=lambda x:(x.d,x.r,x.c))
    r,c=candidate[0].r,candidate[0].c
    people[number].r,people[number].c=r,c
    space[r][c]=-1
    return

while not all_arrived():
    move_people()
    if time<M:
        set_people(time)
    time+=1
print(time)