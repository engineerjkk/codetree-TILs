from collections import deque
import sys
input = sys.stdin.readline
import copy
N_large=5
N_small=3

class Board:
    def __init__(self):
        self.space=[[0]*N_large for _ in range(N_large)]
    
    def in_range(self,r,c):
        return -1<r<N_large and -1<c<N_large
    
    def rotate(self, r, c, cnt):
        result = Board()
        result.space=copy.deepcopy(self.space)
        for _ in range(cnt):
            # sy, sx를 좌측상단으로 하여 시계방향 90도 회전합니다.
            tmp = result.space[r + 0][c + 2]
            result.space[r + 0][c + 2] = result.space[r + 0][c + 0]
            result.space[r + 0][c + 0] = result.space[r + 2][c + 0]
            result.space[r + 2][c + 0] = result.space[r + 2][c + 2]
            result.space[r + 2][c + 2] = tmp
            tmp = result.space[r + 1][c + 2]
            result.space[r + 1][c + 2] = result.space[r + 0][c + 1]
            result.space[r + 0][c + 1] = result.space[r + 1][c + 0]
            result.space[r + 1][c + 0] = result.space[r + 2][c + 1]
            result.space[r + 2][c + 1] = tmp
        return result
    
    def cal_score(self):
        score=0
        visit=[[False]*N_large for _ in range(N_large)]
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(N_large):
            for j in range(N_large):
                if not visit[i][j]:
                    queue=deque()
                    queue.append((i,j))
                    trace=deque()
                    trace.append((i,j))
                    visit[i][j]=True
                    while queue:
                        r,c=queue.popleft()
                        for k in range(4):
                            nr=r+dr[k]
                            nc=c+dc[k]
                            if self.in_range(nr,nc) and self.space[nr][nc]==self.space[r][c] and not visit[nr][nc]:
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
        for j in range(N_large):
            for i in reversed(range(N_large)):
                if self.space[i][j]==0:
                    self.space[i][j]=queue.popleft()

K,M = map(int,input().split())
board=Board()
for i in range(N_large):
    board.space[i]=list(map(int,input().split()))
queue=deque()
for i in list(map(int,input().split())):
    queue.append(i)

for _ in range(K):
    maxScore=0
    maxScoreBoard=None
    for cnt in range(1,4):
        for c in range(3):
            for r in range(3):
                rotated=board.rotate(r,c,cnt)
                score=rotated.cal_score()
                if maxScore<score:
                    maxScore=score
                    maxScoreBoard=rotated
    if maxScoreBoard is None:
        break
    board=maxScoreBoard
    while True:
        board.fill(queue)
        newScore=board.cal_score()
        if newScore==0:
            break
        maxScore+=newScore
    print(maxScore,end=" ")