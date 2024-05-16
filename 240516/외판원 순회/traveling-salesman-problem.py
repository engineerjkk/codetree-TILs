import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
arr=[]
for i in range(1,n):
    arr.append(i)

nCr=list(permutations(arr,n-1))
ans=sys.maxsize
for x in nCr:
    x=list(x)
    x.insert(0,0)
    x.append(0)
    value=0
    for i in range(n):
        r,c=x[i],x[i+1]
        if r==c or lst[r][c]==0:
            value+=sys.maxsize
        else:
            value+=lst[r][c]
    ans=min(ans,value)
print(ans)