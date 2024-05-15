import sys
input = sys.stdin.readline
from itertools import combinations
import math

n,m=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

nCr=combinations(lst,2)
ans=0

def dist(x1,x2,y1,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**(1/2)

for x in nCr:
    distance=dist(x[0][0],x[1][0],x[1][0],x[1][1])
    ans=max(ans,distance)
print(int(ans)**2)