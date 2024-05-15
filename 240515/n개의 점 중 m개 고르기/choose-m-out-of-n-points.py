from itertools import combinations
import sys
n,m=tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

nCr=combinations(lst,m)
ans=0

def dist(x1,x2,y1,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(0.5)
final_ans=sys.maxsize
for x in nCr:
    nXr=list(combinations(x,2))
    for j in nXr:
        distance=dist(j[0][0],j[1][0],j[0][1],j[1][1])
        ans=max(ans,distance)
    final_ans=min(final_ans,ans)
print(round(final_ans**2))