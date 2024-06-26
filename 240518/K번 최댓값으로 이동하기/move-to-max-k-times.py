from collections import deque

n, k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
r,c=map(int,input().split())

queue=deque()
queue.append((r-1,c-1))
dr=[-1,0,1,0]
dc=[0,1,0,-1]
cnt=0
tmp_queue=deque()
while cnt<k:
    if len(queue)==0:
        print(target[1]+1,end=" ")
        print(target[2]+1,end=" ")
        exit()
    else:
        r,c=queue.popleft()
    available=[[False]*n for _ in range(n)]
    available[r][c]=True
    tmp_queue.clear()
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
            if available[i][j]==True and lst[i][j]<lst[r][c]:
                tmp.append([lst[i][j],i,j])
    tmp=sorted(tmp,key=lambda x:(x[0],-x[1],-x[2]),reverse=True)
    if len(tmp)==0:
        print(r+1,end=" ")
        print(c+1,end=" ")
        exit()
    else:
        target=tmp[0]
        queue.append((target[1],target[2]))
        cnt+=1
print(target[1]+1,end=" ")
print(target[2]+1,end=" ")