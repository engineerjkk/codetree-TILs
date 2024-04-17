import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
n,s=map(int,input().split())
lst=list(map(int,input().split()))

nCr=combinations(lst,2)

MIN=1000000

for x in nCr:
    tmp=[]
    for i in lst:
        if i not in x:
            tmp.append(i)
    total=sum(tmp)
    ans=abs(total-s)
    MIN=min(MIN,ans)
print(MIN)