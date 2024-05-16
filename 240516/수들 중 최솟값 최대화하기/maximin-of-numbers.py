import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
arr=[]
for i in range(n):
    arr.append(i)

nCr=permutations(arr,n)

ans=0
for x in nCr:
    tmp=sys.maxsize
    for i,j in zip(arr,x):
        tmp=min(tmp,lst[i][j])
    ans=max(ans,tmp)
print(ans)