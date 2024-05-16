import sys
from itertools import permutations
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input().strip())))

arr=[]
start=[]
end=[]
for i in range(n):
    for j in range(n):
        if lst[i][j] != '.' and lst[i][j] !='S' and lst[i][j] != 'E':
            arr.append([i,j])
        if lst[i][j] == 'S':
            start.append([i,j])
        if lst[i][j] =='E':
            end.append([i,j])

ans=sys.maxsize
if len(arr) < 3:
    print(-1)
    sys.exit(0)
for k in range(3,len(arr)+1):
    nCr=list(permutations(arr,k))
    for x in nCr:
        value=abs(start[0][0]-x[0][0])+abs(start[0][1]-x[0][1])
        cnt=1
        for i in range(1,len(x)):
            r1,c1 = x[i-1]
            r2,c2 = x[i]
            a,b=int(lst[r1][c1]),int(lst[r2][c2])
            if a>b:
                value+=sys.maxsize
            else:
                value+=abs(r1-r2)+abs(c1-c2)
                cnt+=1
        value+=abs(x[-1][0]-end[0][0])+abs(x[-1][1]-end[0][1])
        if cnt<3:
            value+=sys.maxsize
        ans=min(ans,value)
if cnt<3:
    print(-1)
else:
    print(ans)