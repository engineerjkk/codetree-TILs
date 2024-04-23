import sys
input = sys.stdin.readline
from collections import deque
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

dr=[-1,-1,1,1]
dc=[1,-1,-1,1]

def rec(space,r,c):
    visited=[[False]*n for _ in range(n)]
    lst=[]
    lst.append(space[r][c])
    visited[r][c]=True
    for i in range(4):
        while True:
            nr=r+dr[i]
            nc=c+dc[i]
            if -1<nr<n and -1<nc<n and not visited[nr][nc]:
                r=nr
                c=nc
                lst.append(space[r][c])
                visited[nr][nc]=True
            else:
                break
        
    return lst
answer=0
for i in range(n):
    for j in range(n):
        value=rec(space,i,j)
        answer=max(answer,sum(value))
print(answer)