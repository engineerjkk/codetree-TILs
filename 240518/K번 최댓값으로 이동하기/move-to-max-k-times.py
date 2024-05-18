import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

r,c=map(int,input().split())

visited=[False*n for _ in range(n)]
queue=deque()
queue.append((r-1,c-1))
dr=[-1,0,1,0]
dc=[0,1,0,-1]
cnt=0
while cnt<k:
    if len(queue)==0:
        print((target[1],target[2]))
        exit()
    else:
        r,c=queue.popleft()
    available=[[False]*n for _ in range(n)]
    tmp_visited=[[False]*n for _ in range(n)]
    tmp_queue=deque()
    tmp_queue.append((r,c))
    while tmp_queue:
        tmp_r,tmp_c=tmp_queue.popleft()
        for i in range(4):
            nr=tmp_r+dr[i]
            nc=tmp_c+dc[i]
            if -1<nr<n and -1<nc<n and lst[nr][nc]<lst[r][c] and available[nr][nc]==False:
                available[nr][nc]=True
                tmp_queue.append((nr,nc))
    tmp=[]
    for i in range(n):
        for j in range(n):
            if available[i][j]==True:
                tmp.append([lst[i][j],i,j])
    tmp=sorted(tmp,key=lambda x:(x[0],-x[1],-x[2]),reverse=True)
    target=tmp[0]
    queue.append((target[1],target[2]))
    #print(target[1],target[2])
    cnt+=1
print(target[1]+1,end=" ")
print(target[2]+1,end=" ")