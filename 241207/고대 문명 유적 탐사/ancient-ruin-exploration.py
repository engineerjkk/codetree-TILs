import sys
input = sys.stdin.readline
from collections import deque
import copy

K,M=map(int,input().split())

class Board:
    def __init__(self):
        self.space=[[0]*5 for _ in range(5)]
    def rotate(self,cnt,r,c):
        result=Board()
        result.space=copy.deepcopy(self.space)
        for _ in range(cnt):
            tmp=result.space[r+0][c+2]
            result.space[r+0][c+2]=result.space[r+0][c+0]
            result.space[r+0][c+0]=result.space[r+2][c+0]
            result.space[r+2][c+0]=result.space[r+2][c+2]
            result.space[r+2][c+2]=tmp
            tmp=result.space[r+1][c+2]
            result.space[r+1][c+2]=result.space[r+0][c+1]
            result.space[r+0][c+1]=result.space[r+1][c+0]
            result.space[r+1][c+0]=result.space[r+2][c+1]
            result.space[r+2][c+1]=tmp
        return result
    
    def in_range(self,r,c):
        return -1<r<5 and -1<c<5
    
    def cal_score(self):
        score=0
        visit=[[False]*5 for _ in range(5)]
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(5):
            for j in range(5):
                if not visit[i][j]:
                    visit[i][j]=True
                    queue=deque()
                    queue.append((i,j))
                    trace=deque()
                    trace.append((i,j))
                    while queue:
                        r,c=queue.popleft()
                        for k in range(4):
                            nr=r+dr[k]
                            nc=c+dc[k]
                            if self.in_range(nr,nc) and not visit[nr][nc] and self.space[nr][nc]==self.space[r][c]:
                                queue.append((nr,nc))
                                trace.append((nr,nc))
                                visit[nr][nc]=True
                    if len(trace)>=3:
                        score+=len(trace)
                        while trace:
                            r,c=trace.popleft()
                            self.space[r][c]=0
        return score
    
    def fill(self,queue):
        for c in range(5):
            for r in reversed(range(5)):
                if self.space[r][c]==0:
                    self.space[r][c]=queue.popleft()


board=Board()

for i in range(5):
    board.space[i]=list(map(int,input().split()))

queue=deque()
for i in list(map(int,input().split())):
    queue.append(i)

for _ in range(K):
    score=0
    maxScore=0
    maxBoard=None
    for cnt in range(1,4):
        for c in range(3):
            for r in range(3):
                rotated=board.rotate(cnt,r,c)
                newScore=rotated.cal_score()
                if maxScore<newScore:
                    maxScore=newScore
                    maxBoard=rotated
    if maxScore==0 or maxBoard==None:
        break

    board=maxBoard

    while True:
        board.fill(queue)
        newScore=board.cal_score()
        if newScore==0:
            break
        maxScore+=newScore
    print(maxScore,end=" ")




