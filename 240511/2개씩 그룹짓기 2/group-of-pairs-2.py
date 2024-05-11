import sys
input = sys.stdin.readline
from itertools import combinations
n=int(input())
lst=list(map(int,input().split()))

tmp=sorted(lst)
arr=[]
for i in range(n):
    arr.append([tmp[i],tmp[n+i]])
ans=sys.maxsize
for i in range(n):
    x,y=arr[i]
    ans=min(ans,abs(x-y))
print(ans)