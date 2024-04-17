import sys
from itertools import combinations
input = sys.stdin.readline
n,s = map(int,input().split())
lst=list(map(int,input().split()))

nCr = combinations(lst,2)

total_ans=100000
for x in nCr:
    ans=0
    for i in lst:
        if i not in x:
            ans+=i
        
    total_ans=min(total_ans,abs(s-ans))
print(total_ans)