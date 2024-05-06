import sys
input = sys.stdin.readline
from itertools import product
n=int(input())
lst=[]
for i in range(1,n+1):
    lst.append(i)
nCr=product(lst,repeat=n)

ans=0
for x in nCr:
    tmp=True
    for j in x:
        if x.count(j)%j!=0:
            tmp=False
    if tmp:
        ans+=1            
print(ans)