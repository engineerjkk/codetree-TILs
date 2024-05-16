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
#각 행마다 하나의 열만을 가져갈 수 있다.
nCr=permutations(arr,n)
ans=0
for x in nCr:
    value=0
    for i,j in zip(arr,x):
        value+=lst[i][j]
    ans=max(ans,value)
print(ans)