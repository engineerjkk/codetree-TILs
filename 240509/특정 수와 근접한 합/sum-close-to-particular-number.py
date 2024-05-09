import sys
input = sys.stdin.readline
from itertools import combinations
n,s = map(int,input().split())
lst=list(map(int,input().split()))

nCr = combinations(lst,n-2)

ans=sys.maxsize
for x in nCr:
    total=0
    for i in x:
        total+=i
    value=abs(s-total)
    ans=min(ans,value)
print(ans)