import sys
input = sys.stdin.readline
from itertools import combinations
import math

n,m=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

nCr=combinations(lst,m)
ans=sys.maxsize

def dist(x1,x2,y1,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
final_ans=sys.maxsize
for x in nCr:
    nXr=combinations(x,2)
    for j in nXr:
        distance=dist(j[0][0],j[1][0],j[0][1],j[1][1])
        ans=min(ans,distance)
print(int(ans**2))