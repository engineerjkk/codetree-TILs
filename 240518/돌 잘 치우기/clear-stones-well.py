import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy
# n = 격자의 크기, k = 시작 점의 수, m = 꼭 치워야할 돌의 개수
n,k,m = tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

start=[]
for _ in range(k):
    start.append(list(map(int,input().split())))

stone=[]
for i in range(n):
    for j in range(n):
        if lst[i][j]==1:
            stone.append([i,j])
nCr=combinations(stone,m)
dr=[-1,0,1,0]
dc=[0,1,0,-1]
def bfs(tmp,r,c):
    queue=deque()
    queue.append((r,c))
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n and tmp[nr][nc]==0:
                tmp[nr][nc]=2
                queue.append((nr,nc))


ans=0
for x in nCr:
    tmp=copy.deepcopy(lst)
    for i,j in x:
        tmp[i][j]=0
    for r,c in start:
        bfs(tmp,r-1,c-1)
    cnt=0
    for i in range(n):
        for j in range(n):
            if tmp[i][j]==2:
                cnt+=1
    ans=max(ans,cnt)
print(ans)