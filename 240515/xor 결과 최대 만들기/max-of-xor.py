from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
lst=list(map(int,input().split()))

nCr=combinations(lst,m)
ans=0
for x in nCr:
    check=1
    for i in x:
        check^=i
    ans=max(ans,check)
print(ans)