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
    arr=[False]*4
    for num in range(4):
        while True:
            nr=r+dr[num]
            nc=c+dc[num]
            if -1<nr<n and -1<nc<n :
                r=nr
                c=nc
                lst.append(space[r][c])
                arr[num]=True
            else:
                break
    if arr.count(True)==4:
        return lst
    else:
        return [0]
answer=0
for i in range(n):
    for j in range(n):
        value=rec(space,i,j)
        answer=max(answer,sum(value))
print(answer)